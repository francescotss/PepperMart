import os, sys, json, threading
import time


#from playground.modim.src.entity import Product, Entity
pepper_tools_dir = os.getenv('PEPPER_TOOLS_HOME')
sys.path.append(pepper_tools_dir+ '/cmd_server')

#os.environ["PEPPER_IP"] = "172.17.0.2"
os.environ["MODIM_IP"] = "127.0.0.1"

import pepper_cmd
from pepper_cmd import *

from data_handler import *
from modim.scripts.interaction_handler import InteractionHandler

from market import *
from data import * 

global DEBUG
# DEBUG = False
DEBUT = True

def plan_excuter(plan, interaction_handler):
    step_list = plan["plan"]
    
    first_step = step_list[0]
    next_action = plan[first_step]
    interacting = True    
    while interacting:
        action_name = next_action["actions"][0]["name"]
        potential_outcomes = next_action["outcomes"]
        
        # Execute action
        res = interaction_handler.run_action(action_name)
        
        if res == "ERROR" or res == "GOODBYE":
            return
        # Find next action
        for outcome in potential_outcomes:
            if res in outcome["condition"]:
                next_step = outcome["next"]
                if next_step == "GOAL":
                    print("Goal reached")
                    interaction_handler.reset()
                    interacting = False
                else:
                    next_action = plan[next_step]
                
 
 
 
if __name__ == "__main__":
    # Start pepper tools
    begin()

    
    # Read plan
    # TODO: correct file name
    filename = "./pddl/hri_problem_example_v2.json"
    json_data = open(filename).read()
    plan = json.loads(json_data)
    
    # init PepperMarket
    market = Market("./pddl/supermarket_world.pddl", "./pddl/supermarket_problem_template.pddl")
        
    data_dict = {}
    data_dict[PDDL_LABELS.OBJECTS] = objects
    data_dict[PDDL_LABELS.INITS] = inits
    data_dict[PDDL_LABELS.GOALS] = goals
    
    # TODO implements file creation and save the pddl file created in a temp directory
    # market.fill_problem_template(data_dict)

    modim_data = []
    modim_vocabulary = []
    
    for el in inits:
        modim_data_record = None
        modim_vocabulary_record = None
        if el.name == "at" and len(el.args) == 2 and el.args[0].type.name == "product" and el.args[1].type.name == "cell":
            
            # convert to modim format
            position = el.args[1].pos
            position = str(position[0]) + "-" +str(position[1])
            modim_data_record = {
                MODIM_LABELS.TYPE.value: "product",
                MODIM_LABELS.NAME.value: el.args[0].name,
                MODIM_LABELS.POSITION.value: position,
                MODIM_LABELS.CLASSES.value: ""
            }
            
            modim_vocabulary_record = {
                MODIM_LABELS.TYPE.value: "product",
                MODIM_LABELS.WORD.value: el.args[0].name
            }
            modim_data.append(modim_data_record)
            modim_vocabulary.append(modim_vocabulary_record)
    
               
        elif el.name == "is" and len(el.args) == 2 and el.args[0].type.name == "section" and el.args[1].type.name == "cell":
            position = el.args[1].pos
            position = str(position[0]) + "-" +str(position[1])
            modim_data_record = {
                MODIM_LABELS.TYPE.value: "section",
                MODIM_LABELS.NAME.value: el.args[0].name,
                MODIM_LABELS.POSITION.value: position,
                MODIM_LABELS.CLASSES.value: ""
            }
            modim_vocabulary_record = {
                MODIM_LABELS.TYPE.value: "section",
                MODIM_LABELS.WORD.value: el.args[0].name
            }
            modim_data.append(modim_data_record)
            modim_vocabulary.append(modim_vocabulary_record)
       
            
            
        elif el.name == "at" and len(el.args) == 2 and el.args[0].type.name == "human" and el.args[1].type.name == "cell":
            position = el.args[1].pos
            position = str(position[0]) + "-" +str(position[1])
            modim_data_record = {
                MODIM_LABELS.TYPE.value: "human",
                MODIM_LABELS.NAME.value: el.args[0].name,
                MODIM_LABELS.POSITION.value: position,
                MODIM_LABELS.CLASSES.value: ""
            }
            modim_data.append(modim_data_record)
       
            
            
        
    print(modim_data) 
    print(modim_vocabulary)    

    # Start modim and robot
    #data_handler = DataHandler()                    # TODO DELETE
    data_handler = DataHandler(modim_data, modim_vocabulary)
    interaction_handler = InteractionHandler(pepper_cmd.robot, data_handler)
    
    
    
    
    
    # Execution loop
    while True:
        try:
            interaction_handler.init_robot()
            interaction_handler.reset()
            interaction_handler._choose_products()
            exit()
            # Blocking waiting
            interaction_handler.waitfor_person()
            
            # Execute plan
            plan_excuter(plan, interaction_handler)

        except KeyboardInterrupt:
            interaction_handler.shutdown_robot()
            exit()
    
    # Shutdown gracefully            
    interaction_handler.shutdown_robot()
    end()

    
    # cell_1_1 = Entity("1-1", ["walkable"])
    # cell_1_2 = Entity("1-2", ["shelf", "food"])
    # path_1_1 = Entity("1-1", ["path"])
    # start_0_0 = Entity("0-0", ["map-start"])
    # product_1 = Product("eggs", "1-2", [""])
    
    # data_ = {
    #     'tiles': [cell_1_1, cell_1_2, path_1_1, start_0_0],
    #     'products': [product_1]
    # }
    
