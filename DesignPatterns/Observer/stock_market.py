from abc import ABC, abstractmethod


class StockMarket:
    def __init__(self):
        self.observers = []
        self.stocks = {}
        
    def add_observer(self, observer):
        self.observers.append(observer)
        
    def remove_observer(self, observer):
        self.observers.remove(observer)
        
    def add_stock(self, symbol, price):
        self.stocks[symbol] = price
        self.notify(symbol)
        
    def update_stock_price(self, symbol, new_price):
        if symbol in self.stocks:
            self.stocks[symbol] = new_price
            self.notify(symbol)
        
    def notify(self, symbol):
        for observer in self.observers:
            observer.update(symbol, self.stocks[symbol])
            
class Observer(ABC):
    @abstractmethod
    def update(self, symbol, price):
        pass
    
class Investor(Observer):
    def __init__(self, name):
        self.name = name
        
    def update(self, symbol, price):
        print(f"Investor {self.name}: Stock {symbol} price is now {price}")
        
stock_market = StockMarket()


Investor1 = Investor("John")
Investor2 = Investor("Alice")

stock_market.add_observer(Investor1)
stock_market.add_observer(Investor2)

stock_market.add_stock("AAPL", 150.0)
stock_market.add_stock("GOOGL", 2500.64)

