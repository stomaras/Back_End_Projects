import copy

class Document:
    
    def __init__(self, title, content, font, font_size, logo):
        self.title = title
        self.content = content
        self.font = font
        self.font_size = font_size
        self.logo = logo
        
    def __str__(self):
        return f"Title: {self.title}\n" \
               f"Content: {self.content}\n" \
               f"Font: {self.font}\n" \
               f"Font Size: {self.font_size}\n" \
               f"Logo: {self.logo}\n"
    
class DocumentMaker:
    
    def __init__(self):
        self._document = {}
        
    def register_document(self, name, obj):
        self._document[name] = obj
    
    def unregister_document(self, name):
        del self._document[name]
    
    def create_document(self, name, **attrs):
        new_document = copy.deepcopy(self._document.get(name))
        new_document.__dict__.update(attrs)
        return new_document
    
if __name__ == "__main__":
    dm = DocumentMaker()
    
    dm.register_document("doc1", Document("Title 1", "Content 1", "Arial", 12, "Logo 1"))
    dm.register_document("report", Document("Title 2", "Content 2", "Arial", 12, "Logo 2"))
    dm.register_document("presentation", Document("Title 3", "Content 3", "Arial", 21, "Logo 32"))
    
    computer_contract = dm.create_document("report", title="Monthly Report",content="Monthly Financial Report for June 2023")
    monthly_report = dm.create_document("presentation", title="New Product Presentation", content="Intro into our new python product line")
    
    print("--------------Monthly Report---------------")
    print(monthly_report)