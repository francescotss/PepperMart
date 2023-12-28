# PepperMart: A Multimodal Interaction Approach for Shopping Assistant Robots

In this work, we present a proof of concept for a shop assistant robot. This type of system can be employed in various types of shops, including groceries, furniture, electronics, or any medium to large shop open to the public. Our goal is to demonstrate that social robots can play a significant role in our daily lives by collaborating with humans in complex environments. We developed our system for Pepper, a semi-humanoid robot designed to appear friendly and interact naturally with humans using natural language, gestures, vision, and touch. In our application, Pepper serves as a customer receptionist in a grocery store, assisting customers in locating products, creating shopping lists, and registering at the store.


# Features
1. Login/Sign in: In this mode, the robot prompts the user for their name and adds it to the database. If the user is already registered, Pepper facilitates the login process. Additionally, the robot checks if the user has any items on their shopping list and autonomously suggests the optimal route for accessing these products.

2. Find a Product: This action allows users to locate a specific item within the store. Pepper verbally inquires about the product the user is searching for, and the robot subsequently calculates the shortest path in real-time using a classical planning problem generated and solved at runtime.
   
3. Shopping: Reserved exclusively for registered customers, this functionality enables Pepper to assist users in compiling their shopping lists and optimizing their shopping experience. Users can select products either via the tablet interface or by using voice commands. The robot then generates a planning problem, displaying the solution on a map via the tablet. Furthermore, the shopping list is stored in the user’s profile for future reference.

# Instructions
Start naoqi server: /opt/Aldebaran/naoqi-sdk-2.5.5.5-linux64/naoqi
Start modim: cd ~/src/modim/src/GUI && python ws_server.py -robot pepper
Start main: cd ~/playground/ && python main.py 

Generate plan: cd ~/playground/pddl && ../safe-planner/sp ~/playground/pddl/hri_world.pddl ~/playground/pddl/hri_problem.pddl -j -d

To send asr sentence do: cd ~/src/pepper_tools/asr && python human_say.py --sentence "Phrase"
To send fake sonar: cd ~/src/pepper_tools/sonar && python sonar_sim.py --sensor SonarFront --value 1.0 --duration 10.0
