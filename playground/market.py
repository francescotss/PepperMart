from entity import *

from enum import Enum

class LABELS(Enum):
    OBJECTS = "<objects>"
    INITS = "<inits>"
    GOALS = "<goals>"

 
def objects_to_pddl(list :list[Object]):
    pddl = ""
    for e in list:
        pddl += e.to_pddl(True) + " " # "\n"
    return pddl

def inits_to_pddl(list :list[Predicate]):
    pddl = ""
    for e in list:
        pddl += e.to_pddl() + " " # "\n"
    return pddl

def goals_to_pddl(list :list[Object]):
    pddl = ""
    for e in list:
        pddl += e.to_pddl() + " " # "\n"
    return pddl


class Market:
    
    def __init__(self, domain_file, problem_file) -> None:
        self.domain_file = domain_file
        self.problem_file_template = problem_file
        
    def fill_problem_template(self, data):
        
        
        # Opening our text file in read only
        # mode using the open() function
        with open(self.problem_file_template, 'r') as file:
    
            # Reading the content of the file
            # using the read() function and storing
            # them in a new variable
            file_data = file.read()

            # objects
            search_text = LABELS.OBJECTS.value
            replace_text = objects_to_pddl(data[LABELS.OBJECTS])
            # # Searching and replacing the text
            # # using the replace() function
            file_data = file_data.replace(search_text, replace_text)
            
            
            # inits
            search_text = LABELS.INITS.value
            replace_text = inits_to_pddl(data[LABELS.INITS])
            # # Searching and replacing the text
            # # using the replace() function
            file_data = file_data.replace(search_text, replace_text)
            
            
            # goals
            search_text = LABELS.GOALS.value
            replace_text = goals_to_pddl(data[LABELS.GOALS])
            # # Searching and replacing the text
            # # using the replace() function
            file_data = file_data.replace(search_text, replace_text)

        print(file_data)
        


objects = []
inits = []
goals = []

    
human = Object("HUMAN", Type("human"))
cart = Object("CART", Type("cart"))
list = Object("LIST", Type("list"))

cell_5_9 = Object("cell_5_9", Type("cell"))

objects.append(human)
objects.append(cart)
objects.append(list)

inits.append(Predicate("at", [human, cell_5_9]))

# personal_care 
toothpaste = Object("TOOTHPASTE", Type("product"))
shampoo = Object("SHAMPOO", Type("product"))
body_lotion = Object("BODYLOTION", Type("product"))
deodorant  = Object("DEODORAN", Type("product"))

cell_2_4 = Object("cell_2_4",Type("cell"))	
cell_2_5 = Object("cell_2_5",Type("cell"))	
cell_3_4 = Object("cell_3_4",Type("cell"))	
cell_3_5 = Object("cell_3_5",Type("cell"))	

# Predicate("at", toothpaste, cell_2_4)
# Predicate("at", shampoo, cell_2_5)
# Predicate("at", body_lotion, cell_3_4)
# Predicate("at", deodorant, cell_3_5)

objects.append(toothpaste)
objects.append(shampoo)
objects.append(body_lotion)
objects.append(deodorant)

inits.append(Predicate("at", [toothpaste, cell_2_4]))
inits.append(Predicate("at", [shampoo, cell_2_5]))
inits.append(Predicate("at", [body_lotion, cell_3_4]))
inits.append(Predicate("at", [deodorant, cell_3_5]))

# meatcounter 
beef = Object("BEEF", Type("product"))
chicken = Object("CHICKEN", Type("product"))
hamburger = Object("HAMBURGER", Type("product"))

cell_2_2 = Object("cell_2_2",Type("cell"))	
cell_3_2 = Object("cell_3_2",Type("cell"))	

# Predicate("at", beef, cell_2_2)
# Predicate("at", chicken, cell_3_2)
# Predicate("at", hamburger, cell_3_2)

objects.append(beef)
objects.append(chicken)
objects.append(hamburger)

inits.append(Predicate("at", [beef, cell_2_2]))
inits.append(Predicate("at", [chicken, cell_3_2]))
inits.append(Predicate("at", [hamburger, cell_3_2]))

# fishcounter
salmon = Object("SALMON", Type("product"))
tuna = Object("TUNA", Type("product"))
octopus = Object("OCTOPUS", Type("product"))
oyster = Object("OYSTER", Type("product"))

cell_5_2 = Object("cell_5_2",Type("cell"))	
cell_6_2 = Object("cell_6_2",Type("cell"))	

# Predicate("at", salmon, cell_5_2)
# Predicate("at", tuna, cell_5_2)
# Predicate("at", octopus, cell_6_2)
# Predicate("at", oyster, cell_6_2)

objects.append(salmon)
objects.append(tuna)
objects.append(octopus)
objects.append(oyster)

inits.append(Predicate("at", [salmon, cell_5_2]))
inits.append(Predicate("at", [tuna, cell_5_2]))
inits.append(Predicate("at", [octopus, cell_6_2]))
inits.append(Predicate("at", [oyster, cell_6_2]))


# household
eggs = Object("EGGS", Type("product"))
milk = Object("MILK", Type("product"))
bread = Object("BREAD", Type("product"))
cheese = Object("CHEESE", Type("product"))
rice = Object("RICE", Type("product"))
sugar = Object("SUGAR", Type("product"))
salt = Object("SALT", Type("product"))
coffee = Object("COFFEE", Type("product"))
cookies = Object("COOKIES", Type("product"))
ketchup = Object("KETCHUP", Type("product"))


cell_2_7 = Object("cell_2_7",Type("cell"))	
cell_2_8 = Object("cell_2_8",Type("cell"))	
cell_2_9 = Object("cell_2_9",Type("cell"))	
cell_3_7 = Object("cell_3_7",Type("cell"))	
cell_3_8 = Object("cell_3_8",Type("cell"))	
cell_3_9 = Object("cell_3_9",Type("cell"))	

# Predicate("at", eggs, cell_2_7)
# Predicate("at", milk, cell_2_8)
# Predicate("at", bread, cell_2_9)
# Predicate("at", cheese, cell_3_7)
# Predicate("at", rice, cell_3_7)
# Predicate("at", sugar, cell_3_8)
# Predicate("at", salt, cell_3_9)
# Predicate("at", coffee, cell_2_8)
# Predicate("at", cookies, cell_3_8)
# Predicate("at", ketchup, cell_2_9)

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


# beverages
cocacola = Object("COCACOLA", Type("product"))
orangejuice = Object("ORANGEJUICE", Type("product"))
water = Object("WATER", Type("product"))
chinotto = Object("CHINOTTO", Type("product"))

cell_5_4 = Object("cell_5_4",Type("cell"))	
cell_5_5 = Object("cell_5_5",Type("cell"))	
cell_6_4 = Object("cell_6_4",Type("cell"))	
cell_6_5 = Object("cell_6_5",Type("cell"))	

# Predicate("at", cocacola, cell_5_4)
# Predicate("at", water, cell_5_5)
# Predicate("at", chinotto, cell_6_4)
# Predicate("at", orangejuice, cell_6_5)

objects.append(cocacola)
objects.append(orangejuice)
objects.append(water)
objects.append(chinotto)

inits.append(Predicate("at", [cocacola, cell_5_4]))
inits.append(Predicate("at", [water, cell_5_5]))
inits.append(Predicate("at", [chinotto, cell_6_4]))
inits.append(Predicate("at", [orangejuice, cell_6_5]))



# frozen_foods
frozen_pizza = Object("FROZENPIZZA", Type("product"))
frozen_fish = Object("FROZENFISH", Type("product"))
icecream = Object("ICECREAM", Type("product"))
frozen_shrimp = Object("FROZENSHRIMP", Type("product"))
frozen_fish_sticks = Object("FROZENFISHSTICKS", Type("product"))
waffle = Object("WAFFLE", Type("product"))
magnum = Object("MAGNUM", Type("product"))
popsicle = Object("POPSICLE", Type("product"))

cell_8_2 = Object("cell_8_2",Type("cell"))	
cell_8_3 = Object("cell_8_2",Type("cell"))	
cell_8_4 = Object("cell_8_2",Type("cell"))	
cell_8_5 = Object("cell_8_2",Type("cell"))	

cell_9_2 = Object("cell_8_2",Type("cell"))	
cell_9_3 = Object("cell_8_2",Type("cell"))	
cell_9_4 = Object("cell_8_2",Type("cell"))	
cell_9_5 = Object("cell_8_2",Type("cell"))	


# Predicate("at", [frozen_pizza, cell_8_2])
# Predicate("at", [frozen_fish, cell_8_3])
# Predicate("at", [icecream, cell_8_4])
# Predicate("at", [waffle, cell_8_5])
# Predicate("at", [magnum, cell_9_2])
# Predicate("at", [popsicle, cell_9_3])
# Predicate("at", [frozen_shrimp, cell_9_4])
# Predicate("at", [frozen_fish_sticks, cell_9_5])

objects.append(frozen_pizza)
objects.append(frozen_fish)
objects.append(icecream)
objects.append(frozen_shrimp)
objects.append(frozen_fish_sticks)
objects.append(waffle)
objects.append(magnum)
objects.append(popsicle)

inits.append(Predicate("at", [frozen_pizza, cell_8_2]))
inits.append(Predicate("at", [frozen_fish, cell_8_3]))
inits.append(Predicate("at", [icecream, cell_8_4]))
inits.append(Predicate("at", [waffle, cell_8_5]))
inits.append(Predicate("at", [magnum, cell_9_2]))
inits.append(Predicate("at", [popsicle, cell_9_3]))
inits.append(Predicate("at", [frozen_shrimp, cell_9_4]))
inits.append(Predicate("at", [frozen_fish_sticks, cell_9_5]))


# sections
household = Object("household", Type("section"))
personal_care = Object("personal_care", Type("section"))
beverages = Object("beverages", Type("section"))
frozen_foods = Object("frozen_foods", Type("section"))
meatcounter = Object("meatcounter", Type("section"))
fishcounter = Object("fishcounter", Type("section"))
infopoint = Object("infopoint", Type("section"))
cashdesk = Object("cashdesk", Type("section"))
entrace = Object("entrace", Type("section"))
exit = Object("exit", Type("section"))
    
# # example
# inits.append(Predicate("contains", [list, eggs]))
# inits.append(Predicate("contains", [cart, icecream]))
            
# goals.append(Predicate("reached", [human, eggs]))
# goals.append(Predicate("reached", [human, infopoint]))
# goals.append(Predicate("contains", [cart, eggs]))


data_dict = {
    LABELS.OBJECTS: objects,
    LABELS.INITS: inits,
    LABELS.GOALS: goals
}


market = Market("./pddl/supermarket_world.pddl", "./pddl/supermarket_problem_template.pddl")

market.fill_problem_template(data_dict)

# print(objects_to_pddl(objects))
# print(inits_to_pddl(inits))
# print(goals_to_pddl(goals))