# Subject / Observable / Publisher
class Subject:
    def __init__(self):
        self.observers = []
        
    def subscribe(self, observer):
        self.observers.append(observer)
    
    def unsubscribe(self, observer):
        self.observers.remove(observer)
    
    def notify(self, message):
        for observer in self.observers:
            observer.update(message)
            
# Concrete Subject
class WeatherStation(Subject):
    def set_weather(self, weather):
        print("Weather station: Setting weather to", weather)
        self.notify(weather)

# Observer / Subscriber / Listener

class Observer():
    def update(self, message):
        pass
    
class MobileApp(Observer):
    def update(self, message):
        print("Mobile app: Received weather update:", message)
        
class DesktopApp(Observer):
    def update(self, message):
        print("Desktop app: Received weather update:", message)
        
        
# client
weather_station = WeatherStation()

mobile_app = MobileApp()
desktop_app = DesktopApp()


weather_station.subscribe(mobile_app)
weather_station.subscribe(desktop_app)
weather_station.set_weather("Sunny")

weather_station.unsubscribe(desktop_app)
weather_station.set_weather("Cloudy")

 