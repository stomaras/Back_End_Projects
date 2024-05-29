# CPU subsystem --> Memory subsystem --> Other Subsystems --> Computer System

class CPU:
    def freeze(self):
        print("CPU is freezing")
        
    def jump(self, position):
        print(f"Jump to address {position}")
        return position
    
    def execute(self):
        print("Executing code...")
        
class Memory:
    
    def __init__(self):
        self.data = {}
        
    def load(self, position, data):
        print(f"Load data {data} @ address {position}")
        self.data[position] = data
        
    def get_data(self, position):
        print(f"get the data from {position}...")
        return self.data[position]
    
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        
        
    def run(self, program):
        self.cpu.freeze()
        position = 0
        
        for instruction in program:
            self.memory.load(instruction, position)
            self.cpu.jump(position)
            self.cpu.execute()
            position += 1
            
    def retrieve(self, position):
        return self.memory.get_data(position)
    
computer = Computer()
program = [2342,4553,444,'hellow world',252424]
computer.run(program)