from enum import Enum
import json

class MODIM_LABELS(Enum):
    TYPE = "type"
    POSITION = "id"
    CLASSES = "classes"
    NAME = "name"
    WORD = "word"
    
# TODO DELETE
# ID: position
# classes: not-available
MODIM_DATA = [
    {"type": "product","name":"eggs", "id":"1-1", "classes":""},
    {'type': 'human', 'name': 'HUMAN', 'id': '5-9', 'classes': ''},
    {"name":"milk", "id":"1-2", "classes":""},
]

USERS_DATA = {"users": [{"name": "francesco"}]}

PRODUCT_VOCABOLARY = [{"type": "product", "word": "eggs"}, {"type": "section", "word": "infopoint"}]

class DataHandler():
    
    def __init__(self, modim_data, vocabulary):
        self.modim_data = modim_data
        self.product_vocabulary = vocabulary

        with open('users.json', 'r') as userfile:
            data = json.load(userfile)
            self.userlist = data["users"]
            
    def get_user(self, name):
        for user in self.userlist:
            print("USER", user)
            if user["name"] == name:
                return user
        return None
    
    def create_user(self, name):
        user = {"name": name}
        self.userlist["users"].append(user)
        
        with open('users.json', 'w') as userfile:
            json.dump(self.userlist, userfile)
        
    
    # def __init__(self):    
    #     self.map_list = MAP_LIST                # TODO DELETE
    #     self.product_list = PRODUCT_LIST        # TODO DELETE
    #     self.product_vocabolary = PRODUCT_VOCABOLARY    # TODO DELETE
    
    def reset_map(self, modim_data):
        self.modim_data = modim_data
       
    # def reset_map(self):
    #     self.map_list = MAP_LIST                # TODO DELETE
    #     self.product_list = PRODUCT_LIST        # TODO DELETE
        
    def get_product_list(self):
        return self.product_list
    
    def get_product_vocabulary(self):
        ret = []
        for prod in self.product_vocabulary:
            if prod["type"] == "product":
                ret.append(prod["word"])
        return ret
    
    def get_product(self,name):
        for product in self.product_list:
            if product["name"] == name: return product
        return None
    
    def add_product_class(self, product, cls):
        product = self.get_product(product)
        product["classes"] += cls
        
    def set_product_class(self, product, cls):
        product = self.get_product(product)
        product["classes"] = cls
    
    def get_map_data(self):
        return {"tiles": self.map_list, "products": self.product_list}      # TODO DELETE
    
    # def get_map_data(self):    
    #     retrun self.modim_data