import os, sys, json
pepper_tools_dir = os.getenv('PEPPER_TOOLS_HOME')
sys.path.append(pepper_tools_dir+ '/cmd_server')

#os.environ["PEPPER_IP"] = "172.17.0.2"
os.environ["MODIM_IP"] = "127.0.0.1"

import pepper_cmd
from pepper_cmd import *

from data_handler import DataHandler
from modim.scripts.interaction_handler import InteractionHandler

global DEBUG
DEBUG = True

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
        
        # Find next action
        for outcome in potential_outcomes:
            if res == outcome["condition"][0]:
                next_step = outcome["next"]
                if next_step == "GOAL":
                    print("Goal reached")
                    interacting = False
                else:
                    next_action = plan[next_step]
                
 
 
 
if __name__ == "__main__":
    # Start pepper tools
    begin()

    # Start modim and robot
    data_handler = DataHandler()
    interaction_handler = InteractionHandler(pepper_cmd.robot, data_handler)
    interaction_handler.init_robot()
    
    # Read plan
    # TODO: correct file name
    filename = "./pddl/hri_proplem_example.json"
    json_data = open(filename).read()
    plan = json.loads(json_data)
    
    # Execute plan
    plan_excuter(plan, interaction_handler)

    # Stop pepper tools
    end()