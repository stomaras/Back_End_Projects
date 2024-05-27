# In python, a class can act as a decorator if it has a __call__ method.
# The __call__ method is invoked when an instance of the class is called as a function.
# This allows us to define a callable object that can modify the behavior of another function or class.

class Decorator:
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        print("Before calling")
        result = self.func(*args, **kwargs)
        print("After calling")
        return result
    
@Decorator
def greeting():
    print("Hello World")
    
greeting()