import os, sys, json, inspect
pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')
from ws_client import *
import ws_client


class Modim():
    
    
    def __init__(self, robot, product_vocabolary=None):
        self.mws = ModimWSClient()
        self.mws.setDemoPathAuto(__file__)
        self.robot = robot
        self.product_vocabolary = product_vocabolary
        
    def home(self):
        def _func():
            im.init()
        self.mws.run_interaction(_func)
   
    def show_path(self, data=None):
        
        with open('modim/actions/mapdata', 'w') as action_file:
            json_text = str(data) #json.dumps(data) Not working: modim will remove the double quotes. 
            text = "TEXT_mapdata\n<*,*,*,*>: " + json_text + "\n----"
            action_file.write(text)

        def _func():
            im.display.loadUrl('map.html')
            im.execute('mapdata') 
            im.execute('showPath')
            

        self.mws.run_interaction(_func)

        
        timeout = 30 
        answer = self.robot.asr(self.product_vocabolary,timeout)
        if answer!="":
            print(answer)
    