from abc import ABC, abstractmethod

# Visitor Interface
class DocumentVisitor(ABC):
    @abstractmethod
    def visit_paragraph(self, paragraph):
        pass
    
    @abstractmethod
    def visit_heading(self, heading):
        pass
    
    
class WordCount(DocumentVisitor):
    def __init__(self):
        self.word_count = 0
        
    def visit_paragraph(self, paragraph):
        words = len(paragraph.text.split())
        self.word_count += words

    def visit_heading(self, heading):
        words = len(heading.text.split())
        self.word_count += words


# it allows users to create a document with different elements such as paragraphs headings and images
class DocumentElement(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


# Concrete Element: Paragraph
class Paragraph(DocumentElement):
    def __init__(self,text):
        self.text = text

    def accept(self, visitor):
        visitor.visit_paragraph(self)

class Heading(DocumentElement):
    def __init__(self, text):
        self.text = text
        
    def accept(self, visitor):
        visitor.visit_heading(self)


# Document class
class Document:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)
        
    def process(self, visitor):
        for element in self.elements:
            element.accept(visitor)
            
            
# Client Code

if __name__ == '__main__':
    document = Document()
    
    document.add_element(Paragraph("This is a paragraph"))
    document.add_element(Heading("Heading 1"))
    
    
    word_counter = WordCount()
    
    document.process(word_counter)
    print(f"Word Count: {word_counter.word_count}")