import os, sys, json, inspect, textwrap, time
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
        self.interaction_started = False
        self.user_logged = False
        self.user_name = None
        self.product_asked = None
         
    def init_robot(self):
        def _func():
            im.init()
        self.mws.run_interaction(_func)
        
        if not DEBUG:
            self.robot.setLanguage("en")
            self.robot.setAlive(True)
            self.robot.startFaceDetection()
            self.robot.startSensorMonitor() 
            self.robot.startLaserMonitor()
    
    def shutdown_robot(self):
        if not DEBUG:
            self.robot.stopFaceDetection()      
            self.robot.stopSensorMonitor()
            self.robot.stopLaserMonitor()
            self.robot.setAlive(False)
        
    def reset(self):
        self.data.reset_map()
        self.user_logged = False
        self.user_name = None
        self.product_asked = None
            
    def is_person_here(self):
        activation_zone = 1.2 # distance in meters
        if DEBUG:
            return True
        values = self.robot.sensorvalue()
        laser = values[0]
        sonar = values[1]
        rear_sonar = values[2]
        return 0 < laser < activation_zone or 0 < sonar < activation_zone
        
    def waitfor_person(self):
        if DEBUG: return
        
        start_time = None
        wait_time = 2.0 # Time to wait before starting the interaction
        utils.color_print("Waiting for person", "yellow")
        while True:
            if self.is_person_here():
                if start_time is None:
                    start_time = time.time()
                elif time.time() - start_time > wait_time:
                    utils.color_print("Person detected", "green")
                    return # Person detected for wait_time seconds
            if not self.is_person_here():
                start_time = None
            time.sleep(0.5)    
    
    def waitfor_goodbye(self):
        if DEBUG: return False
        
        start_time = None
        wait_time = 3.0 # Time to wait before choose to say goodbye
        utils.color_print("Waiting to see if the person is gone", "yellow")
        while True:
            if not self.is_person_here():
                if start_time is None:
                    start_time = time.time()
                elif time.time() - start_time > wait_time:
                    utils.color_print("Person not detected", "red")
                    return True # Person not detected for wait_time seconds
            if self.is_person_here():
                utils.color_print("Person detected", "green")
                return False
            time.sleep(0.5)  
        
                
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
        if not self.is_person_here() and self.waitfor_goodbye():
            return "GOODBYE"
            
        utils.color_print("\n\n\nExecuting action {} \n".format(action), "green")
        if action == "robot_say_welcome":
            res =  self._robot_say_welcome()
        elif action == "robot_wait_human_decision" or action == "robot_wait_human_decision_registered":
            res =  self._robot_wait_human_decision()
        elif action == "robot_do_registration":
            res = self._robot_do_registration()
        elif action == "robot_do_info":
            res = self._robot_do_info()
        elif action == "robot_do_where":
            res = self._robot_do_where()
        elif action == "do_shopping":
            res = self._shopping()  
        
        utils.color_print("\nEnd action {}".format(action), "green")
        return res
        
        
    
        
    
    
    # -------- Action Handlers -------- #
    
    def _robot_say_welcome(self):
        def _welcome_callback():
            im.display.loadUrl('index.html')
            im.execute('welcome')
        def _welcomeBack_callback():
            im.display.loadUrl('index.html')
            im.execute('welcomeBack')
        
        if not self.interaction_started:
            self.send_interaction(_welcome_callback)
            self.interaction_started = True
        else:
            self.send_interaction(_welcomeBack_callback)
        
        return  "(can_wait_welcome human)"
    
    def _robot_wait_human_decision(self):
        def _modim_callback():
            im.execute('welcomeBack')
            im.executeModality('ASR',vocabulary)
            answer = im.ask(actionname=None, timeout=5) 
            time.sleep(0.6) # Wait for asr thread shutdown
            im.display.setReturnValue(answer)

    
        help_voc = ["help", "what can you do", "what can i ask"]
        registration_voc = ["register", "sign in"]
        shopping_voc = ["shopping", "cart"]
        where_voc = ["where"] + utils.build_vocabolary(["where"], self.data.product_vocabolary)
        vocabulary = help_voc + registration_voc + shopping_voc + where_voc
        
        answer = self.send_interaction(_modim_callback, [["vocabulary", vocabulary]])
        
        if answer == 'timeout':
            return self.run_action("robot_wait_human_decision")
               
        if answer == "ERROR":
            return "ERROR"
        
        elif answer in help_voc:
            return "(human_say_info human)"
        
        elif answer in registration_voc:
            if self.user_logged:
                self.robot.say("Hi %s, you are already registered!" %self.user_name)
                return "(can_wait_welcome human)"
            return "(human_say_registration human)"
        
        elif answer in shopping_voc:
            if not self.user_logged:
                self.robot.say("I'm sorry, you must be registered")
                return "(can_wait_welcome human)"
            return "(human_say_shopping human)"
        
        elif answer in where_voc:
            # answer: where + product
            answer = answer.split(" ")
            if len(answer) > 1:
                self.product_asked = answer[1]
            return "(human_say_where human)"
        
        
    
    def _robot_do_registration(self):
        
        self.user_logged = True
        return "(human_is_registered human)"  
    
    def _robot_do_info(self):
        return "(interaction_start human robot)"
    
    def _robot_do_where(self):
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
        utils.create_mapdata_file(map_data)
        self.robot.asay("Check the map to find the {}".format(self.product_asked))            
        self.mws.run_interaction(_modim_callback)
        self.data.reset_map()  
              
        return "(interaction_done human robot)"
    
    
    def _choose_products(self, single_mode=False):
        def _show_interface():
            im.display.loadUrl('products.html')
            im.executeModality('BUTTONS', buttons)
            im.executeModality('BUTTONS_continue', ["continue", "Continue"])
            if single_mode:
                im.execute('chooseProduct')
            else:
                im.execute('chooseProducts')

        def _ask_callback():
            im.executeModality('BUTTONS', buttons)
            im.executeModality('BUTTONS_continue', ["continue", "Continue"])
            im.executeModality('ASR',vocabulary)
            answer = im.ask(actionname=None, timeout=10) 
            time.sleep(0.5) # Wait for asr thread shutdown
            im.display.setReturnValue(answer)
            
        product_buttons = []
        for product in self.data.get_product_vocabulary():
            button = [product, product.capitalize()]
            product_buttons.append(button)  
        self.send_interaction(_show_interface, [["buttons", product_buttons], ["single_mode", single_mode]])
        
        
        vocabulary = self.data.get_product_vocabulary()
        continue_voc = ["done", "that's all", "continue"]
        vocabulary += continue_voc
        
        selected = []
        while True:
            product = self.send_interaction(_ask_callback, [["vocabulary", vocabulary ], ["buttons", product_buttons]])
            if product in continue_voc:
                return selected
            if product == 'timeout':
                continue
            selected.append(product)
            if single_mode:
                return selected[0]
            elif len(selected) == 1:
                self.robot.say("I've added the %s to your shopping cart. What else?" %product)
            else:
                self.robot.say("%s added" %product)
                
        
        
        
    
    def _shopping(self):
        self._choose_products()
        return "(interaction_done human robot)"
      
   
   
   
   
   
   
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
    