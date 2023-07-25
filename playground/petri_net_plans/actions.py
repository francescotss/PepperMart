import os, sys

pdir = os.getenv('PNP_HOME')
sys.path.insert(0, pdir+'/PNPnaoqi/actions/')

import action_base
from action_base import *


class WelcomeAction(NAOqiAction_Base):
    
    def __init__(self, actionName, session, modim):
        NAOqiAction_Base.__init__(self,actionName, session)
        
        self.modim = modim

    def actionThread_exec (self, params):
        # action exec
        print("Action "+self.actionName+" "+params+" exec...")
        
        #  
        
        # action end
        action_termination(self.actionName,params)

class WelcomeRegistrationAction(NAOqiAction_Base):
    
    def __init__(self, actionName, session, modim):
        NAOqiAction_Base.__init__(self,actionName, session)
        
        self.modim = modim

    def actionThread_exec (self, params):
        # action exec
        print("Action "+self.actionName+" "+params+" exec...")
        
        # 
        
        # action end
        action_termination(self.actionName,params)

class WelcomeShoppingAction(NAOqiAction_Base):
    
    def __init__(self, actionName, session, modim):
        NAOqiAction_Base.__init__(self,actionName, session)
        
        self.modim = modim

    def actionThread_exec (self, params):
        # action exec
        print("Action "+self.actionName+" "+params+" exec...")
        
        # 
        
        # action end
        action_termination(self.actionName,params)

class WelcomeWhereAction(NAOqiAction_Base):
    
    def __init__(self, actionName, session, modim):
        NAOqiAction_Base.__init__(self,actionName, session)
        
        self.modim = modim

    def actionThread_exec (self, params):
        # action exec
        print("Action "+self.actionName+" "+params+" exec...")
        
        # 
        
        # action end
        action_termination(self.actionName,params)
