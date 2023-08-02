from enum import Enum

class PDDL_LABELS(Enum):
    OBJECTS = "<objects>"
    INITS = "<inits>"
    GOALS = "<goals>"

def objects_to_pddl(list):
    pddl = ""
    for e in list:
        pddl += e.to_pddl(True) + " " # "\n"
    return pddl

def inits_to_pddl(list):
    pddl = ""
    for e in list:
        pddl += e.to_pddl() + " " # "\n"
    return pddl

def goals_to_pddl(list):
    pddl = ""
    for e in list:
        pddl += e.to_pddl() + " " # "\n"
    return pddl


class Market:
    
    def __init__(self, domain_file, problem_file):
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

        print(file_data)
        


