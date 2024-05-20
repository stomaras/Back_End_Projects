import copy

class GameObject:
    
    def __init__(self, name):
        self.name = name
        
    def clone(self):
        return copy.deepcopy(self)
    
class Character(GameObject):
    def __init__(self, name, health):
        super().__init__(name)
        self.health = health
        
class Enemy(GameObject):
    def __init__(self, name, strength):
        super().__init__(name)
        self.strength = strength
        
class GameEngine:
    def __init__(self):
        self.prototype_objects = {}
        
    def register_prototype(self, name, prototype):
        self.prototype_objects[name] = prototype
        
    def create_game_object(self, name):
        prototype = self.prototype_objects.get(name)
        if prototype:
            return prototype.clone()
        else:
            raise ValueError(f"Prototype with key {name} does not exist")
        
engine = GameEngine()

#Register Prototypes
character_prototype = Character("Player", 100)
engine.register_prototype("player", character_prototype)

enemy_proto = Enemy("Enemy", 50)
engine.register_prototype("enemy", enemy_proto)

# Create game objects
player = engine.create_game_object("player")
player.health = 150

enemy = engine.create_game_object("enemy")
enemy.strength = 75

# Print object details
print("{} with Strength:{}".format(player.health, enemy.strength))
print("{} with Strength:{}".format(enemy.name, enemy.strength))