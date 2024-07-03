from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def display(self):
        pass
    
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()
        
    def display(self):
        print(f"Displaying {self.filename}")
        
    def load_from_disk(self):
        print(f"Loading {self.filename} from disk...")
        
        
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None
        
    def display(self):
        if not self.real_image:
            self.real_image = RealImage(self.filename)
            
        self.real_image.display()
        
        
# client code

image1 = ProxyImage("image1.jpg")
image2 = ProxyImage("image2.jpg")

image1.display()
image2.display()