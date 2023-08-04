from enum import Enum
import json, os

class MODIM_LABELS(Enum):
    TYPE = "type"
    POSITION = "id"
    CLASSES = "classes"
    NAME = "name"
    

class PDDL_LABELS(Enum):
    OBJECTS = "<objects>"
    INITS = "<inits>"
    GOALS = "<goals>"
    ENTITIES = "<entities>"
    
    
from entity import *


# map_data = [
#      {'classes': '', 'type': 'section', 'name': 'cashdesk', 'id': '9-7'}, 
#      {'classes': '', 'type': 'section', 'name': 'cashdesk', 'id': '9-9'}, 
#      {'classes': '', 'type': 'product', 'name': 'EGGS', 'id': '9-9'},
#      {'classes': '', 'type': 'human', 'name': 'HUMAN', 'id': '9-9'},
     
# ]

# vocabulary_data = [
#      {'type': 'section', 'word': 'cashdesk'}, 
#      {'type': 'section', 'word': 'cashdesk'}, 
#      {'type': 'product', 'word': 'EGGS'},
# ]


class DataHandler():
    
    def __init__(self, pddl_generator):
        
        self.pddl_generator = pddl_generator
        self.data = initialization() # init data
        self.map_data = []
        self.vocabulary_data = []
        self.user_data = None
        
        self.init_map()
        self.init_users()
        
        
    def init_users(self):
        with open('users.json', 'r') as userfile:
            self.user_data = json.load(userfile)
            
    def init_map(self):     
        # fill map and vocabulary using data given by the initilization() function
        for el in self.data[PDDL_LABELS.INITS]:
            map_record = None
            vocabulary_record = None
            if el.name == "at" and len(el.args) == 2 and el.args[0].type.name == "product" and el.args[1].type.name == "cell":
                # convert to modim format
                position = el.args[1].pos
                position = str(position[0]) + "-" +str(position[1])
                map_record = {
                    MODIM_LABELS.TYPE.value: "product",
                    MODIM_LABELS.NAME.value: el.args[0].name,
                    MODIM_LABELS.POSITION.value: position,
                    MODIM_LABELS.CLASSES.value: ""
                }
                
                vocabulary_record = {
                    MODIM_LABELS.TYPE.value: "product",
                    MODIM_LABELS.NAME.value: el.args[0].name
                }
                
                self.map_data.append(map_record)
                self.vocabulary_data.append(vocabulary_record)
        
                
            elif el.name == "is" and len(el.args) == 2 and el.args[1].type.name == "section" and el.args[0].type.name == "cell":
                position = el.args[0].pos
                position = str(position[0]) + "-" +str(position[1])
                map_record = {
                    MODIM_LABELS.TYPE.value: "section",
                    MODIM_LABELS.NAME.value: el.args[1].name,
                    MODIM_LABELS.POSITION.value: position,
                    MODIM_LABELS.CLASSES.value: ""
                }
                vocabulary_record = {
                    MODIM_LABELS.TYPE.value: "section",
                    MODIM_LABELS.NAME.value: el.args[1].name
                }
                self.map_data.append(map_record)
                self.vocabulary_data.append(vocabulary_record)
                
                
            elif el.name == "at" and len(el.args) == 2 and el.args[0].type.name == "human" and el.args[1].type.name == "cell":
                position = el.args[1].pos
                position = str(position[0]) + "-" +str(position[1])
                map_record = {
                    MODIM_LABELS.TYPE.value: "human",
                    MODIM_LABELS.NAME.value: el.args[0].name,
                    MODIM_LABELS.POSITION.value: position,
                    MODIM_LABELS.CLASSES.value: ""
                }
                self.map_data.append(map_record)
        
        # print(self.map_data)
        # print(self.vocabulary_data)
            
    def reset(self):
        self.data = initialization()
        self.map_data = []
        self.vocabulary_data = []
        self.user_data = None
        self.init_users()
        self.init_map()
            
    # [GOAL]
    # (reached HUMAN fishcounter)
    def set_where_goal(self, product_section_list):
        goals = []
        human = self.data[PDDL_LABELS.ENTITIES][0]
        # LIST = self.data[PDDL_LABELS.ENTITIES][1]
        # CART = self.data[PDDL_LABELS.ENTITIES][2]
        
        for element in product_section_list:
            for obj in self.data[PDDL_LABELS.OBJECTS]:
                if obj.name == element[MODIM_LABELS.NAME.value]:
                    goals.append(Predicate("reached", [human, obj]))
        
        self.update_structure(goals, PDDL_LABELS.GOALS)
                    
            
      
    # [INIT]  
    # (contains CART p1 )
    # [GOAL]
    # (contains LIST p1 )          
    def set_shopping_goal(self, product_list):
        inits = []
        goals = []
        # HUMAN = self.data[PDDL_LABELS.ENTITIES][0]
        LIST = self.data[PDDL_LABELS.ENTITIES][1]
        CART = self.data[PDDL_LABELS.ENTITIES][2]
        
        for element in product_list:
            for obj in self.data[PDDL_LABELS.OBJECTS]:
                if obj.name == element[MODIM_LABELS.NAME.value]:
                    inits.append(Predicate("contains", [LIST, obj]))
                    goals.append(Predicate("contains", [CART, obj]))     
        self.update_structure(inits, PDDL_LABELS.INITS)
        self.update_structure(goals, PDDL_LABELS.GOALS)
                    
    def update_structure(self, objects, structure_identifier):
        for o in objects:
            self.data[structure_identifier].append(o)

    def create_map_record(self, type, name, position, classes):
        map_record = {
                    MODIM_LABELS.TYPE.value: type,
                    MODIM_LABELS.NAME.value: name,
                    MODIM_LABELS.POSITION.value: position,
                    MODIM_LABELS.CLASSES.value: classes
                }
        return map_record
        
    
    # TODO THIS FUNCTION SHOULD BE CALLED ONE TIMES FOR EACH HUMAN INTERACTION
    def solve_problem(self):
        self.pddl_generator.fill_problem_template(self.data)
        # Planner needs the absolute path :(
        os.system("cd ~/playground/pddl/temp && ../../safe-planner/sp ~/playground/pddl/supermarket_world.pddl ~/playground/pddl/temp/supermarket_problem.pddl -j -d") 
                    
    def update_map_data(self):
        with open('pddl/temp/supermarket_problem.json', 'r') as jsonfile:
            plan = json.load(jsonfile)
            step_list = plan["plan"]
            
            for step in step_list:
                action = plan[step]["actions"][0]
                name = action["name"]
                args = action["arguments"]
                position = self.position_pddl_to_modim(args[-1])
                map_entry = self.get_map_by_id(position)
                
                if name == "move":
                    if len(map_entry) == 0:
                        map_entry = self.create_map_record("cell", "", position, "path")
                        self.map_data.append(map_entry)
                    else:
                        map_entry[0]["classes"] += " path"
                        
                elif name == "take":
                    for entry in map_entry:
                        if entry["name"].lower() == args[-2]:
                            entry["classes"] += " take"
                 
                
    def position_pddl_to_modim(self, pos):
        _, y, x = pos.split("_")
        return (y+"-"+x).encode('ascii')            
    
        
    def get_user(self, name):
        for user in self.user_data:
            if user["name"].encode('ascii') == name:
                return user
        return None
    
    def create_user(self, name):
        user = {"name": name}
        self.user_data.append(user)  
        with open('users.json', 'w') as userfile:
            json.dump(self.user_data, userfile)
    
    def save_product_list(self, user, products):
        user["shopping_list"] = products
        with open('users.json', 'w') as userfile:
            json.dump(self.user_data, userfile)
            
    def get_product_vocabulary(self):
        ret = []
        for prod in self.vocabulary_data:
            if prod[MODIM_LABELS.TYPE.value] == "product":
                ret.append(prod[MODIM_LABELS.NAME.value])
        return ret    
    
    def get_section_vocabulary(self):
        ret = []
        for prod in self.vocabulary_data:
            if prod[MODIM_LABELS.TYPE.value] == "section":
                ret.append(prod[MODIM_LABELS.NAME.value])
        return ret 
    
    def get_map(self, update=False):
        if update:
            self.update_map_data()
        return self.map_data
    
    def get_map_by_id(self, id):
        ret = []
        for prod in self.map_data:
            if prod[MODIM_LABELS.POSITION.value] == id:
                ret.append(prod)
        return ret
    
    def get_map_by_name(self, name):
        ret = []
        for prod in self.map_data:
            if prod[MODIM_LABELS.NAME.value] == name:
                ret.append(prod)
        return ret
    

class PDDLGenerator:
    
    def __init__(self, domain_file, problem_file_template, temp_problem_file_path):
        self.domain_file = domain_file
        self.problem_file_template = problem_file_template
        self.temp_problem_file_path = temp_problem_file_path
    
    # USE THIS FUNCTION ONE TIMES FOR EACH HUMAN INTERACTION    
    def fill_problem_template(self, data):
        
        
        # Opening our text file in read only
        # mode using the open() function
        with open(self.problem_file_template, 'r') as problem_file_template:
    
            # Reading the content of the file
            # using the read() function and storing
            # them in a new variable
            file_data = problem_file_template.read()
            problem_file_template.close()

            # objects
            search_text = PDDL_LABELS.OBJECTS.value
            replace_text = objects_to_pddl(data[PDDL_LABELS.OBJECTS])
            # # Searching and replacing the text
            # # using the replace() function
            file_data = file_data.replace(search_text, replace_text)
            
            
            # inits
            search_text = PDDL_LABELS.INITS.value
            replace_text = inits_to_pddl(data[PDDL_LABELS.INITS])
            # # Searching and replacing the text
            # # using the replace() function
            file_data = file_data.replace(search_text, replace_text)
            
            
            # goals
            search_text = PDDL_LABELS.GOALS.value
            replace_text = goals_to_pddl(data[PDDL_LABELS.GOALS])
            # # Searching and replacing the text
            # # using the replace() function
            file_data = file_data.replace(search_text, replace_text)

        # print(file_data)
        
        problem_file = open(self.temp_problem_file_path, "w")
        problem_file.write(file_data)
        problem_file.close()


def objects_to_pddl(list):
    pddl = ""
    for e in list:
        pddl += "\t\t" + e.to_pddl(True) + "\n"
    return pddl

def inits_to_pddl(list):
    pddl = ""
    for e in list:
        pddl +=  "\t\t" + e.to_pddl() + "\n"
    return pddl

def goals_to_pddl(list):
    pddl = ""
    for e in list:
        pddl +=  "\t\t" + e.to_pddl() + "\n"
    return pddl

    
def initialization():
    
    objects = []
    inits = []
    goals = []
    
    entities = []

    # OBJECTS 
    
    # - entities
    human = Object("HUMAN", Type("human"))
    shopping_list = Object("LIST", Type("list"))
    shopping_cart = Object("CART", Type("cart"))
    
    entities.append(human)
    entities.append(shopping_list)
    entities.append(shopping_cart)
    
    # - sections
    household = SectionObject("household" )
    personal_care = SectionObject("personalcare" )
    beverages = SectionObject("beverages" )
    frozen_foods = SectionObject("frozenfoods" )
    meatcounter = SectionObject("meatcounter" )
    fishcounter = SectionObject("fishcounter" )
    infopoint = SectionObject("infopoint" )
    cashdesk = SectionObject("cashdesk" )
    start_point = SectionObject("entrace" )
    end_point = SectionObject("exit")

    
    # personal_care 
    toothpaste = ProductObject("TOOTHPASTE")
    shampoo = ProductObject("SHAMPOO")
    body_lotion = ProductObject("BODYLOTION")
    deodorant  = ProductObject("DEODORAN")
    
    # meatcounter 
    beef = ProductObject("BEEF")
    chicken = ProductObject("CHICKEN")
    hamburger = ProductObject("HAMBURGER")
    
    # fishcounter
    salmon = ProductObject("SALMON")
    tuna = ProductObject("TUNA")
    octopus = ProductObject("OCTOPUS")
    oyster = ProductObject("OYSTER")
    
    # household
    eggs = ProductObject("EGGS" )
    milk = ProductObject("MILK" )
    bread = ProductObject("BREAD" )
    cheese = ProductObject("CHEESE" )
    rice = ProductObject("RICE" )
    sugar = ProductObject("SUGAR" )
    salt = ProductObject("SALT" )
    coffee = ProductObject("COFFEE" )
    cookies = ProductObject("COOKIES" )
    ketchup = ProductObject("KETCHUP" )
    
    # beverages
    cocacola = ProductObject("COCACOLA" )
    orangejuice = ProductObject("ORANGEJUICE" )
    water = ProductObject("WATER" )
    chinotto = ProductObject("CHINOTTO" )
    
    # frozen_foods
    frozen_pizza = ProductObject("FROZENPIZZA" )
    frozen_fish = ProductObject("FROZENFISH" )
    icecream = ProductObject("ICECREAM" )
    frozen_shrimp = ProductObject("FROZENSHRIMP" )
    frozen_fish_sticks = ProductObject("FROZENFISHSTICKS" )
    waffle = ProductObject("WAFFLE" )
    magnum = ProductObject("MAGNUM" )
    popsicle = ProductObject("POPSICLE" )
    
    
    # - cells
    cell_8_2 = CellObject("cell_8_2", (8, 2))	
    cell_8_3 = CellObject("cell_8_2", (8, 3))	
    cell_8_4 = CellObject("cell_8_2", (8, 4))	
    cell_8_5 = CellObject("cell_8_2", (8, 5))	

    cell_9_2 = CellObject("cell_8_2", (9, 2))	
    cell_9_3 = CellObject("cell_8_2", (9, 3))	
    cell_9_4 = CellObject("cell_8_2", (9, 4))	
    cell_9_5 = CellObject("cell_8_2", (9, 5))	

    cell_5_4 = CellObject("cell_5_4", (5, 4))	
    cell_5_5 = CellObject("cell_5_5", (5, 5))	
    cell_6_4 = CellObject("cell_6_4", (6, 4))	
    cell_6_5 = CellObject("cell_6_5", (6, 5))	

    cell_2_7 = CellObject("cell_2_7", (2, 7))	
    cell_2_8 = CellObject("cell_2_8", (2, 8))	
    cell_2_9 = CellObject("cell_2_9", (2, 9))	
    cell_3_7 = CellObject("cell_3_7", (3, 7))	
    cell_3_8 = CellObject("cell_3_8", (3, 8))	
    cell_3_9 = CellObject("cell_3_9", (3, 9))	

    cell_5_2 = CellObject("cell_5_2", (5, 2))	
    cell_6_2 = CellObject("cell_6_2", (6, 2))

    cell_2_2 = CellObject("cell_2_2", (2, 2))	
    cell_3_2 = CellObject("cell_3_2", (3, 2))	
	

    cell_2_4 = CellObject("cell_2_4", (2, 4))	
    cell_2_5 = CellObject("cell_2_5", (2, 5))	
    cell_3_4 = CellObject("cell_3_4", (3, 4))	
    cell_3_5 = CellObject("cell_3_5", (3, 5))	
    
    cell_9_7 = CellObject("cell_9_7", (9, 7))
    cell_9_9 = CellObject("cell_9_9", (9, 9))
    
    cell_7_7 = CellObject("cell_7_7", (7, 7))
    cell_7_8 = CellObject("cell_7_8", (7, 8))
    cell_7_9 = CellObject("cell_7_9", (7, 9))
 
    cell_5_9 = CellObject("cell_5_9", (5, 9))

    # append objects
    objects.append(human)
    objects.append(shopping_cart)
    objects.append(shopping_list)
    
    objects.append(toothpaste)
    objects.append(shampoo)
    objects.append(body_lotion)
    objects.append(deodorant)
    
    objects.append(beef)
    objects.append(chicken)
    objects.append(hamburger)
    
    objects.append(salmon)
    objects.append(tuna)
    objects.append(octopus)
    objects.append(oyster)
    
    objects.append(eggs)
    objects.append(milk)
    objects.append(bread)
    objects.append(cheese)
    objects.append(rice)
    objects.append(sugar)
    objects.append(salt)
    objects.append(coffee)
    objects.append(cookies)
    objects.append(ketchup)
    
    objects.append(cocacola)
    objects.append(orangejuice)
    objects.append(water)
    objects.append(chinotto)
    
    objects.append(frozen_pizza)
    objects.append(frozen_fish)
    objects.append(icecream)
    objects.append(frozen_shrimp)
    objects.append(frozen_fish_sticks)
    objects.append(waffle)
    objects.append(magnum)
    objects.append(popsicle)
        
    objects.append(household)
    objects.append(personal_care)
    objects.append(beverages)
    objects.append(frozen_foods)
    objects.append(meatcounter)
    objects.append(fishcounter)
    objects.append(infopoint)
    objects.append(cashdesk)
    objects.append(start_point)
    objects.append(end_point)


    # append predicates
    inits.append(Predicate("at", [human, cell_5_9]))

    inits.append(Predicate("at", [toothpaste, cell_2_4]))
    inits.append(Predicate("at", [shampoo, cell_2_5]))
    inits.append(Predicate("at", [body_lotion, cell_3_4]))
    inits.append(Predicate("at", [deodorant, cell_3_5]))
    
    inits.append(Predicate("at", [beef, cell_2_2]))
    inits.append(Predicate("at", [chicken, cell_3_2]))
    inits.append(Predicate("at", [hamburger, cell_3_2]))

    inits.append(Predicate("at", [salmon, cell_5_2]))
    inits.append(Predicate("at", [tuna, cell_5_2]))
    inits.append(Predicate("at", [octopus, cell_6_2]))
    inits.append(Predicate("at", [oyster, cell_6_2]))

    inits.append(Predicate("at", [eggs, cell_2_7]))
    inits.append(Predicate("at", [milk, cell_2_8]))
    inits.append(Predicate("at", [bread, cell_2_9]))
    inits.append(Predicate("at", [cheese, cell_3_7]))
    inits.append(Predicate("at", [rice, cell_3_7]))
    inits.append(Predicate("at", [sugar, cell_3_8]))
    inits.append(Predicate("at", [salt, cell_3_9]))
    inits.append(Predicate("at", [coffee, cell_2_8]))
    inits.append(Predicate("at", [cookies, cell_3_8]))
    inits.append(Predicate("at", [ketchup, cell_2_9]))

    inits.append(Predicate("at", [cocacola, cell_5_4]))
    inits.append(Predicate("at", [water, cell_5_5]))
    inits.append(Predicate("at", [chinotto, cell_6_4]))
    inits.append(Predicate("at", [orangejuice, cell_6_5]))

    inits.append(Predicate("at", [frozen_pizza, cell_8_2]))
    inits.append(Predicate("at", [frozen_fish, cell_8_3]))
    inits.append(Predicate("at", [icecream, cell_8_4]))
    inits.append(Predicate("at", [waffle, cell_8_5]))
    inits.append(Predicate("at", [magnum, cell_9_2]))
    inits.append(Predicate("at", [popsicle, cell_9_3]))
    inits.append(Predicate("at", [frozen_shrimp, cell_9_4]))
    inits.append(Predicate("at", [frozen_fish_sticks, cell_9_5]))

    inits.append(Predicate("is", [cell_2_2, meatcounter]))
    inits.append(Predicate("is", [cell_3_2, meatcounter]))
    inits.append(Predicate("is", [cell_5_2, fishcounter]))
    inits.append(Predicate("is", [cell_6_2, fishcounter]))
            
    inits.append(Predicate("is", [cell_2_4, personal_care]))
    inits.append(Predicate("is", [cell_3_4, personal_care]))
    inits.append(Predicate("is", [cell_2_5, personal_care]))
    inits.append(Predicate("is", [cell_3_5, personal_care]))   
            
    inits.append(Predicate("is", [cell_2_7, household]))
    inits.append(Predicate("is", [cell_3_7, household]))
    inits.append(Predicate("is", [cell_2_8, household])) 
    inits.append(Predicate("is", [cell_3_8, household]))
    inits.append(Predicate("is", [cell_2_9, household]))
    inits.append(Predicate("is", [cell_3_9, household]))
            
    inits.append(Predicate("is", [cell_8_2, frozen_foods])) 
    inits.append(Predicate("is", [cell_9_2, frozen_foods]))
    inits.append(Predicate("is", [cell_9_3, frozen_foods])) 
    inits.append(Predicate("is", [cell_9_3, frozen_foods]))
    inits.append(Predicate("is", [cell_8_4, frozen_foods])) 
    inits.append(Predicate("is", [cell_9_4, frozen_foods]))
    inits.append(Predicate("is", [cell_8_5, frozen_foods])) 
    inits.append(Predicate("is", [cell_9_5, frozen_foods]))

    inits.append(Predicate("is", [cell_5_4, beverages])) 
    inits.append(Predicate("is", [cell_6_4, beverages]))
    inits.append(Predicate("is", [cell_5_5, beverages])) 
    inits.append(Predicate("is", [cell_6_5, beverages]))

    inits.append(Predicate("is", [cell_7_7, infopoint])) 
    inits.append(Predicate("is", [cell_7_8, infopoint])) 
    inits.append(Predicate("is", [cell_7_9, infopoint]))

    inits.append(Predicate("is", [cell_9_7, cashdesk])) 
    inits.append(Predicate("is", [cell_9_9, cashdesk]))


    # # GOALS
    # # example of usage with CONTAINS GOAL
    # inits.append(Predicate("contains", [shopping_list, eggs]))
    # inits.append(Predicate("contains", [shopping_list, eggs]))
    # inits.append(Predicate("contains", [shopping_list, eggs]))
    # inits.append(Predicate("contains", [shopping_list, eggs]))
    # inits.append(Predicate("contains", [shopping_list, eggs]))
    # inits.append(Predicate("contains", [shopping_list, eggs]))
    # inits.append(Predicate("contains", [shopping_list, eggs]))

    # goals.append(Predicate("contains", [shopping_cart, eggs]))
    # goals.append(Predicate("contains", [shopping_cart, eggs]))
    # goals.append(Predicate("contains", [shopping_cart, eggs]))
    # goals.append(Predicate("contains", [shopping_cart, eggs]))
    # goals.append(Predicate("contains", [shopping_cart, eggs]))
    # goals.append(Predicate("contains", [shopping_cart, eggs]))
    # goals.append(Predicate("contains", [shopping_cart, eggs]))
               
    # # example of usage with REACHED GOAL         
    # goals.append(Predicate("reached", [human, meatcounter]))
    
    data = {
        PDDL_LABELS.INITS: inits,
        PDDL_LABELS.OBJECTS: objects,
        PDDL_LABELS.GOALS: goals,
        PDDL_LABELS.ENTITIES: entities
    }
    
    return data



