 
class Entity:
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
        super().__init__(_id, _classes)
        self._name = _name
        
    def to_string(self):
        return super().to_string() + " name: " + self._name

    # def to_pddl_object()
     
     
     
# pddl interface
class Type:
    def __init__(self, name : str):
        self.name = name
        
class Object:
    def __init__(self, name : str, type : Type) -> None:
        self.name = name
        self.type = type
        
    def to_pddl(self, type=False):
        if type:
            return self.name + " - " + self.type.name 
        else:
            return self.name
    
class Predicate:
    def __init__(self, name : str, args : list[Object]) -> None:
        self.name = name
        self.args = args
    
    def to_pddl(self):
        pddl = ""
        pddl += "(" + self.name
        for a in self.args:
            pddl += " " + a.name
        pddl += ")"
        return pddl