import os, sys
pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')
from ws_client import *
import ws_client


class Modim():
    
    
    def __init__(self):
        self.mws = ModimWSClient()
        self.mws.setDemoPathAuto(__file__)
        
        
    def home(self):
        def _func():
            #im.display.loadUrl('index.html')
            im.init()
            #im.execute('welcome')
        self.mws.run_interaction(_func)
   
        
    def welcome(self):
        def _func():
            im.display.loadUrl('index.html')
            im.execute('welcome')
        self.mws.run_interaction(_func)
        