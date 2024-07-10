# state draft -> Review -> Finalize -> Published
from abc import ABC, abstractmethod

class DocumentState(ABC):
    @abstractmethod
    def process_document(self, document):
        pass
    
class DraftState(DocumentState):
    def process_document(self, document):
        print("Process document draft state") 
        document.state = ReviewState()
    
class ReviewState(DocumentState):
    def process_document(self, document):
        print("Process document review state")
        document.state = FinalizeState()
    
class FinalizeState(DocumentState):
    def process_document(self, document):
        print("Process document finalize state")  # Assume document is finalized here and marked as published state
        document.state = PublishedState()
    
class PublishedState(DocumentState):
    def process_document(self, document):
        print("Document is already finalized")  # Assume document is published here

# context - document
class Document:
    def __init__(self):
        self.state = DraftState()

    def process(self):
        self.state.process_document(self)
        
document = Document()
document.process()
document.process()
document.process()
document.process()
document.process()