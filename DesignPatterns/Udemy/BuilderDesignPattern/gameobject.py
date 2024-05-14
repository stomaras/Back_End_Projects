class GameOject:
    def __init__(self):
        self.transform:Transform = None
        self.renderer:Renderer = None
        self.collider:Collider = None
        self.script:str = None
        
    def __str__(self):
        return f"Transform: {self.transform}\n Renderer:{self.renderer}\n Collider: {self.collider}\n Script: {self.script}\n"
    
class Transform:
    def __init__(self, position:tuple, rotation:tuple, scale:tuple) -> None:
        self.position = position
        self.rotation = rotation
        self.scale = scale
        
    def __str__(self):
        return f"Position: {self.position}, Rotation: {self.rotation}, Scale: {self.scale}"
    
class Renderer:
    def __init__(self, mesh:str, material:str):
        self.mesh = mesh
        self.material = material
        
    def __str__(self):
        return f"Mesh: {self.mesh}, Material:{self.material}"
    
class Collider:
    def __init__(self, shape:str, is_trigger:bool):
        self.shape = shape
        self.is_trigger = is_trigger
        
    def __str__(self) -> str:
        return f"Shape: {self.shape}, Trigger:{self.is_trigger}"
    
class GameBuilder:
    def __init__(self) -> None:
        self._game = GameOject()
        
    def add_transform(self, position, rotation, scale):
        self._game.transform = Transform(position, rotation, scale)
        
    def add_renderer(self, mesh, material):
        self._game.renderer = Renderer(mesh, material)
        
    def add_collider(self, shape, is_trigger):
        self._game.collider = Collider(shape, is_trigger)
        
    def add_script(self, script):
        self._game.script = script
        
    def get_game(self):
        return self._game
    
print("===============================ENGINE 1=================================")
builder = GameBuilder()
builder.add_transform((1,2,3),(4,6,2),(5,6,3))
builder.add_renderer("CubeMesh","DefaultBlackShine")
builder.add_collider("Box", False)
builder.add_script("TurnScript.js")

game1 = builder.get_game()
print(game1)

print("==============================ENGINE 2====================================")
builder2 = GameBuilder()
builder2.add_transform((10,12,23),(5,22,15),(14,9,7))
builder2.add_renderer("Cylinder", "DarkCloud")
builder2.add_collider("Circle", True)
builder2.add_script("ManualTurner")

game2 = builder2.get_game()
print(game2)



