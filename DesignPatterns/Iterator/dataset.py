class RecordIterator:
    def __init__(self, records):
        self.records = records
        self.index = 0
        
    def has_next(self):
        return self.index < len(self.records)
    
    def next(self):
        if self.has_next():
            record = self.records[self.index]
            self.index += 1
            return record
        else:
            raise StopIteration()
        
class DatabaseResultSet:
    def __init__(self, result_set):
        self.result_set = result_set
    
    def get_iterator(self):
        return RecordIterator(self.result_set)


result_set = [
    {"id":1, "name":"john", "age":30},
    {"id":2, "name":"Alice", "age":23},
    {"id":3, "name":"Tom", "age":32},
]



record_set = DatabaseResultSet(result_set)
iterator = record_set.get_iterator()


while iterator.has_next():
    record = iterator.next()
    print(record)