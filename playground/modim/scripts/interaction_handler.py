import os, sys, json, inspect, textwrap
pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')
from ws_client import *
import ws_client
import utils
global DEBUG
DEBUG = True


class InteractionHandler():
    
    def __init__(self, robot, data):
        self.mws = ModimWSClient()
        self.mws.setDemoPathAuto(__file__)
        self.robot = robot
        self.data = data
        self.product_asked = None
        
    def init_robot(self):
        def _func():
            im.init()
        self.mws.run_interaction(_func)
        
        if not DEBUG:
            self.robot.setLanguage("en")
            self.robot.setAlive(True)
            self.robot.startSensorMonitor() 
            self.robot.startLaserMonitor()
        
    def send_interaction(self, code, vars=[]):
        self.mws.code = ""
        for var, value in vars:
            self.mws.setGlobalVar(var, value)
        
        lcode = inspect.getsourcelines(code)
        locode = ""
        for l in lcode[0][1:]:
            locode += l
        self.mws.code += textwrap.dedent(locode)
        self.mws.cconnect()
        print(self.mws.code)
        return self.mws.csend(self.mws.code)

        
    def run_action(self, action):
        utils.color_print("\n\n\nExecuting action {} \n".format(action), "green")
        if action == "robot_say_welcome":
            res =  self._welcome()
        elif action == "do_registration":
            res = self._registration()
        elif action == "do_info":
            res = self._info()
        elif action == "do_where":
            res = self._where()
        elif action == "do_shopping":
            res = self._shopping()  
        
        utils.color_print("\nEnd action {}".format(action), "green")
        return res
        
    
        
    
    
    # -------- Action Handlers -------- #
    
    def _welcome(self):
        def _modim_callback():
            im.display.loadUrl('index.html')
            im.execute('welcome')
            a = im.ask(actionname=None, timeout=-1)  

        ret = self.send_interaction(_modim_callback)

        print(ret)
        
        # TODO: Build vocabolary
        help_voc = ["help", "what can you do", "what can i ask"]
        registration_voc = ["register", "signin"]
        shopping_voc = ["shopping", "cart"]
        where_voc = ["where"] + utils.build_vocabolary(["where"], self.data.product_vocabolary)
        vocabulary = help_voc + registration_voc + shopping_voc
        
        answer = utils.ask_loop(vocabulary, self.robot, timeout=10, patience=2)
           
        if answer == "ERROR":
            return "ERROR"
        
        elif answer in help_voc:
            return "(telling_info human)"
        
        elif answer in registration_voc:
            return "(telling_registration human)"
        
        elif answer in shopping_voc:
            return "(telling_shopping human)"
        
        elif answer in where_voc:
            # answer: where + product
            answer = answer.split(" ")
            if len(answer) > 1:
                self.product_asked = answer[1]
            return "(telling_where human)"
        
        
    
    def _registration(self):
        return "(telling_registration human)"  
    
    def _info(self):
        return ""
    
    def _where(self):
        def _modim_callback():
            im.display.loadUrl('map.html')
            im.execute('mapdata')
            im.execute('showProduct')
            
        if self.product_asked is None:
            self.robot.asay("What are you looking for?")
            answer = utils.ask_loop(self.data.product_vocabolary, self.robot)
            if answer == "ERROR":
                return "ERROR"
            self.product_asked = answer
        
        self.data.add_product_class(self.product_asked,"show")
        map_data = self.data.get_map_data()
        utils.create_data_file(map_data)
        self.robot.asay("Check the map to find the {}".format(self.product_asked))            
        self.mws.run_interaction(_modim_callback)
        self.data.reset_map()  
              
        return "(interaction_done human)"
    
    def _shopping(self):
        return
      
   
    def show_path(self, data=None):

        def _func():
            im.display.loadUrl('map.html')
            im.execute('mapdata') 
            im.execute('showPath')
            

        self.mws.run_interaction(_func)

        
        timeout = 30 
        answer = self.robot.asr(self.product_vocabolary,timeout)
        if answer!="":
            print(answer)
    