# Iterator implements __next__(), __iter__()
# Iterator takes in an iterable (list, tuple, string) as parameter
class MyIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.keys = list(iterable.keys())
        self.index = 0
        
    def __next__(self):
        if self.has_next():
            key = self.keys[self.index]
            value = self.iterable[key]
            self.index += 1
            return key, value
        else:
            raise StopIteration
    
    def has_next(self):
        return self.index < len(self.iterable)
    
    def __iter__(self):
        return self


# Iterable - List, tuple, dictionary etc.
if __name__ == '__main__':
    
    lst = ['sofa','Deji','Maxwell','Simon']
    
    lst4 = {"name":"Sola", "age":32, "gender":"Male","level":300}
    
    iterator = MyIterator(lst4)
    
    for key, value in iterator:
        print(f'Key: {key}, Value: {value}')