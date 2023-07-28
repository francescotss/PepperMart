from modim.scripts import *
import os, sys
pdir = os.getenv('PNP_HOME')
sys.path.insert(0, pdir+'/PNPnaoqi/py')

import pnp_cmd_naoqi
from pnp_cmd_naoqi import *

from petri_net_plans import *



modim_client = modim.Modim()
# modim_client.home()


# app = action_base.initApp()

# WelcomeAction('welcome', app.session, modim_client)
# WelcomeRegistrationAction('welcome registration', app.session, modim_client)
# WelcomeShoppingAction('welcome shopping', app.session, modim_client)
# WelcomeWhereAction('welcome where', app.session, modim_client)


# app.run() # blocking

p = PNPCmd()

p.begin()

p.plan_cmd('myplan', 'start')

# to = 3
# while (not 'goal' in p.plan_status() and to>0):
#     print(p.plan_name(), p.plan_status())
#     # time.sleep(0.5)
#     to -= 0.5

print(p.plan_name(), p.plan_status())

p.plan_cmd('myplan', 'stop')


p.end()



