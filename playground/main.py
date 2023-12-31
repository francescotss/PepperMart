import os, sys, json

pepper_tools_dir = os.getenv('PEPPER_TOOLS_HOME')
sys.path.append(pepper_tools_dir+ '/cmd_server')

#os.environ["PEPPER_IP"] = "172.17.0.2"
os.environ["MODIM_IP"] = "127.0.0.1"

import pepper_cmd
from pepper_cmd import *

from data_handler import *
from modim.scripts.interaction_handler import InteractionHandler

global DEBUG
DEBUG = False


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
        
        if res == "ERROR":
            interaction_handler.error()
            return
        if res == "GOODBYE":
            interaction_handler.goodbye()
            return
            
            
        # Find next action
        for outcome in potential_outcomes:
            if res in outcome["condition"]:
                next_step = outcome["next"].encode('ascii')
                if next_step == "GOAL":
                    print("Goal reached")
                    interaction_handler.goal()
                    interacting = False
                else:
                    next_action = plan[next_step]
                
 
 
 
if __name__ == "__main__":
    # Start pepper tools
    begin()

    
    # Read plan
    # TODO: correct file name
    filename = "./pddl/hri_problem.json"
    json_data = open(filename).read()
    plan = json.loads(json_data)
    
    
    # init PepperMarket
    generator = PDDLGenerator("./pddl/supermarket_world.pddl", "./pddl/supermarket_problem_template.pddl", "./pddl/temp/supermarket_problem.pddl")
    
    # Start modim and robot
    data_manager = DataHandler(generator)
    interaction_handler = InteractionHandler(pepper_cmd.robot, data_manager)
    
    # Execution loop
    while True:
        try:
            interaction_handler.init_robot()
            interaction_handler.reset()
                        
            # Blocking waiting
            interaction_handler.waitfor_person()
            
            
            # Execute plan
            plan_excuter(plan, interaction_handler)

        except KeyboardInterrupt:
            interaction_handler.shutdown_robot()
            exit()
    
