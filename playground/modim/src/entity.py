 
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

    

        
