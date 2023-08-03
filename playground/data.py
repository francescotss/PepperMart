from entity import *

objects = []
inits = []
goals = []

    
human = Object("HUMAN", Type("human"))
cart = Object("CART", Type("cart"))
list = Object("LIST", Type("list"))

cell_5_9 = CellObject("cell_5_9", (5, 9))

objects.append(human)
objects.append(cart)
objects.append(list)

inits.append(Predicate("at", [human, cell_5_9]))

# personal_care 
toothpaste = ProductObject("TOOTHPASTE")
shampoo = ProductObject("SHAMPOO")
body_lotion = ProductObject("BODYLOTION")
deodorant  = ProductObject("DEODORAN")

cell_2_4 = CellObject("cell_2_4", (2, 4))	
cell_2_5 = CellObject("cell_2_5", (2, 5))	
cell_3_4 = CellObject("cell_3_4", (3, 4))	
cell_3_5 = CellObject("cell_3_5", (3, 5))	

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
beef = ProductObject("BEEF")
chicken = ProductObject("CHICKEN")
hamburger = ProductObject("HAMBURGER")

cell_2_2 = CellObject("cell_2_2", (2, 2))	
cell_3_2 = CellObject("cell_3_2", (3, 2))	

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
salmon = ProductObject("SALMON")
tuna = ProductObject("TUNA")
octopus = ProductObject("OCTOPUS")
oyster = ProductObject("OYSTER")

cell_5_2 = CellObject("cell_5_2", (5, 2))	
cell_6_2 = CellObject("cell_6_2", (6, 2))	

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


cell_2_7 = CellObject("cell_2_7", (2, 7))	
cell_2_8 = CellObject("cell_2_8", (2, 8))	
cell_2_9 = CellObject("cell_2_9", (2, 9))	
cell_3_7 = CellObject("cell_3_7", (3, 7))	
cell_3_8 = CellObject("cell_3_8", (3, 8))	
cell_3_9 = CellObject("cell_3_9", (3, 9))	

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
cocacola = ProductObject("COCACOLA" )
orangejuice = ProductObject("ORANGEJUICE" )
water = ProductObject("WATER" )
chinotto = ProductObject("CHINOTTO" )

cell_5_4 = CellObject("cell_5_4", (5, 4))	
cell_5_5 = CellObject("cell_5_5", (5, 5))	
cell_6_4 = CellObject("cell_6_4", (6, 4))	
cell_6_5 = CellObject("cell_6_5", (6, 5))	

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
frozen_pizza = ProductObject("FROZENPIZZA" )
frozen_fish = ProductObject("FROZENFISH" )
icecream = ProductObject("ICECREAM" )
frozen_shrimp = ProductObject("FROZENSHRIMP" )
frozen_fish_sticks = ProductObject("FROZENFISHSTICKS" )
waffle = ProductObject("WAFFLE" )
magnum = ProductObject("MAGNUM" )
popsicle = ProductObject("POPSICLE" )

cell_8_2 = CellObject("cell_8_2", (8, 2))	
cell_8_3 = CellObject("cell_8_2", (8, 3))	
cell_8_4 = CellObject("cell_8_2", (8, 4))	
cell_8_5 = CellObject("cell_8_2", (8, 5))	

cell_9_2 = CellObject("cell_8_2", (9, 2))	
cell_9_3 = CellObject("cell_8_2", (9, 3))	
cell_9_4 = CellObject("cell_8_2", (9, 4))	
cell_9_5 = CellObject("cell_8_2", (9, 5))	


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
household = SectionObject("household" )
personal_care = SectionObject("personal_care" )
beverages = SectionObject("beverages" )
frozen_foods = SectionObject("frozen_foods" )
meatcounter = SectionObject("meatcounter" )
fishcounter = SectionObject("fishcounter" )
infopoint = SectionObject("infopoint" )
cashdesk = SectionObject("cashdesk" )
entrace = SectionObject("entrace" )
exit = SectionObject("exit" )
    
# # example
# inits.append(Predicate("contains", [list, eggs]))
# inits.append(Predicate("contains", [cart, icecream]))
            
# goals.append(Predicate("reached", [human, eggs]))
# goals.append(Predicate("reached", [human, infopoint]))
# goals.append(Predicate("contains", [cart, eggs]))

