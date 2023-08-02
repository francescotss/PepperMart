 
class Entity(object):
    def __init__(self, _position, _classes):
        self._position = _position
        self._classes = _classes
    
    def to_string(self):
        return "id: " + self._position[0] + "-" + self._position[1] + " classes: " + [c + " " for c in self._classes];
            
    
    def to_json(self):
        json = "{ " + self.to_string() + " }";
        return json

    
class Product(Entity):
    def __init__(self, _name, _id, _classes):
        super(Product, self).__init__(_id, _classes)
        self._name = _name
        
    def to_string(self):
        return super().to_string() + " name: " + self._name

    # def to_pddl_object()
     
    
# pddl interface
class Type:
    def __init__(self, name):
        self.name = name
        
class Object(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
    def to_pddl(self, type=False):
        if type:
            return self.name + " - " + self.type.name 
        else:
            return self.name
        
class CellObject(Object):
    def __init__(self, name, pos):
        super(CellObject, self).__init__(name, Type("cell"))
        self.pos = pos

class ProductObject(Object):
    def __init__(self, name):
        super(ProductObject, self).__init__(name, Type("product"))
        

class SectionObject(Object):
    def __init__(self, name):
        super(SectionObject, self).__init__(name, Type("section"))


class Predicate:
    def __init__(self, name, args):
        self.name = name
        self.args = args
    
    def to_pddl(self):
        pddl = ""
        pddl += "(" + self.name
        for a in self.args:
            pddl += " " + a.name
        pddl += ")"
        return pddl