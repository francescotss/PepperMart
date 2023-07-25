from modim.scripts import *
import os, sys
pdir = os.getenv('PNP_HOME')
sys.path.insert(0, pdir+'/PNPnaoqi/py')

import pnp_cmd_naoqi
from pnp_cmd_naoqi import *


from petri_net_plans import *



# modim_client = modim.Modim()
# modim_client.home()
modim_client = None

app = action_base.initApp()

WelcomeAction('welcome', app.session, modim_client)
WelcomeRegistrationAction('welcome_registration', app.session, modim_client)
WelcomeShoppingAction('welcome_shopping', app.session, modim_client)
WelcomeWhereAction('welcome_where', app.session, modim_client)


app.run() # blocking

# p = PNPCmd()

# p.begin()

# p.exec_action('WelcomeAction', '3') # blocking

# p.exec_action('welcome', '5')

# # p.execute_plan('myplan') # blocking

# # p.start_plan('myplan') # non-blocking


# # p.stop_plan('myplan')

p.end()



