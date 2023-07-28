from modim.scripts import *
import os, sys
pepper_tools_dir = os.getenv('PEPPER_TOOLS_HOME')
sys.path.append(pepper_tools_dir+ '/cmd_server')

import pepper_cmd
from pepper_cmd import *


def plan_excuter(plan):
    



if __name__ == "__main__":
    # Start pepper tools
    begin()

    # Start modim
    m = modim.Modim(pepper_cmd.robot)


    data = {
        'tiles': [{"id": "1-1", "classes": "walkable"}, {"id": "1-2", "classes": "shelf food"}, {"id": "1-1", "classes": "path"}, {"id": "0-0", "classes": "map-start"}],
        "products": [{"id": "1-2", "name": "eggs", "classes": ""}]
        }
    m.show_path(data)

    # Stop pepper tools
    end()