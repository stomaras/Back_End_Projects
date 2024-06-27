from abc import ABC, abstractmethod

class WeatherStation:
    def __init__(self):
        self.observers = []
        self.weather_data = {}
        
        
    def attach(self, observer): #subscribe for notification
        self.observers.append(observer)
        
    def detach(self, observer): #unsubscribe for notification
        self.observers.remove(observer)
        
    def set_weather(self, temperature, humidity, pressure):
        self.weather_data['temperature'] = temperature
        self.weather_data['humidity'] = humidity
        self.weather_data['pressure'] = pressure
        self.notify()
        
    def notify(self): #notify all observers about the change
        for observer in self.observers:
            observer.update(self.weather_data)
            
    
class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass
    
class DisplayDevice(Observer):
    def __init__(self,name):
        self.name = name
    
    def update(self, weather_data):
        print(f"{self.name} received weather data: - Temperature: {weather_data['temperature']}C, Humidity: {weather_data['humidity']}, Pressure: {weather_data['pressure']}")

class PrintDevice(Observer):
    def update(self, weather_data):
        pass
    
    
# client

weather_station = WeatherStation()

# observer
display1 = DisplayDevice("Living Room Display")
display2 = DisplayDevice("Bed Room Display")

weather_station.attach(display1)
weather_station.attach(display2)

weather_station.set_weather(25,70,100)


