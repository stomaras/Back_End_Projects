
class Singleton:
    __instance = None
    
    @staticmethod
    def getInstance(name):
        if Singleton.__instance is None:
            Singleton(name)
        return Singleton.__instance
        
        
    def __init__(self, name):
        self.name = name
        if Singleton.__instance is not None:
            raise Exception("Instance already exists!")
        Singleton.__instance = self
        
ns1 = Singleton.getInstance("Boy")
ns2 = Singleton.getInstance("Girl")

print(ns1 is ns2)