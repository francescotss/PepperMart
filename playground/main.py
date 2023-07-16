from modim.scripts import *
import os, sys
pdir = os.getenv('PNP_HOME')
sys.path.insert(0, pdir+'/PNPnaoqi/py')
import pnp_cmd_naoqi
from pnp_cmd_naoqi import *

m = modim.Modim()
m.home()