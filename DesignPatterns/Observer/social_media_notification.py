from abc import ABC, abstractmethod
class SocialMediaSubject: # publusher / subject / observer
    def __init__(self):
        self.observers = []
        self.posts = []
        
    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)
       
    # the method will fire that notification to all the observers that are waiting for it. 
    def add_post(self, post):
        self.posts.append(post)
        self.notify(post)
        
    def notify(self, post):
        for observer in self.observers:
            observer.update(post)
            
class Observer(ABC):
    @abstractmethod
    def update(self, post):
        pass
    
    
class User(Observer):
    def __init__(self, name):
        self.name = name
        
    def update(self, post):
        print(f"User {self.name} received a new post: {post}")
        
        
# client 
social_media = SocialMediaSubject()

user1 = User("ChrisTsek10")
user2 = User("zarmakoupes")
user3 = User("Chris_Fragoulis_")
user4 = User("KwstasKrs")



social_media.attach(user1)
social_media.attach(user2)
social_media.attach(user3)
social_media.attach(user4)

social_media.add_post("Today, I've eaten some delicious pancakes!")
social_media.add_post("I just had a great weekend!")