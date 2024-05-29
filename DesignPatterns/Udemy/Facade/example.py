# Complex System
class SubSystemA:
    def operationA1(self):
        print("SubSystemA operationA1")
        
    def operationA2(self):
        print("SubSystemA operationA2")
        
class SubSystemB:
    def operationB1(self):
        print("SubSystemB operationB1")
        
    def operationB2(self):
        print("SubSystemB operationB2")
        
# Facade
class Facade:
    def __init__(self):
        self.subsystemA = SubSystemA()
        self.subsystemB = SubSystemB()
        
    def operation1(self):
        self.subsystemA.operationA1()
        self.subsystemB.operationB1()
        
    def operation2(self):
        self.subsystemA.operationA2()
        self.subsystemB.operationB2()
        
if __name__ == "__main__":
    facade = Facade()
    facade.operation1()
    facade.operation2()
    