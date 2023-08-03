MAP_LIST = [
    {"id": "1-1", "classes": "walkable"}, 
    {"id": "1-2", "classes": "shelf food"}, 
    {"id": "1-1", "classes": "path"}, 
    {"id": "0-0", "classes": "map-start"}
]


# ID: position
# classes: not-available
PRODUCT_LIST = [
    {"name":"eggs", "id":"1-1", "classes":""},
    {"name":"milk", "id":"1-2", "classes":""},
]


PRODUCT_VOCABULARY = ["eggs", "milk"]

class DataHandler():
    
    def __init__(self):
        self.map_list = MAP_LIST
        self.product_list = PRODUCT_LIST
        self.product_vocabulary = PRODUCT_VOCABULARY
        
    def reset_map(self):
        self.map_list = MAP_LIST
        self.product_list = PRODUCT_LIST 
        
    def get_product_list(self):
        return self.product_list
    
    def get_product_vocabulary(self):
        return self.product_vocabulary
    
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
        return {"tiles": self.map_list, "products": self.product_list}