# To perfrom operations like data analysis, diagnosis and patient record processing on various medical data , such as 
# symptoms, test results and medical history.

# Medical Information System
# Medical data elements: [Symptom, Test results, Medical History] (Elements)
# Operations: [Data Analyser, Diagnostic, Record Processing] (Visitors) on a symptom, on a test results

from abc import ABC,abstractmethod

class MedicalInformationSystem:
    def __init__(self):
        self.medical_data = []
        
    def add_medical_data(self, data):
        self.medical_data.append(data)
    
    # e.g take symptoms and do medical analysis on it, take test results and do mecial analysis on it
    def process_data(self, visitor):
        for data in self.medical_data:
            data.accept(visitor)
            
# Element Interface
class MedicalData(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass
    
# Concrete Element: Symptoms
class Symptoms(MedicalData):
    def accept(self, visitor):
        visitor.visit_symptoms(self)
        
# Concrete Element: Test Results
class TestResults(MedicalData):
    def accept(self, visitor):
        visitor.visit_test_results(self)
        
# Concrete Element: MedicalHistory
class MedicalHistory(MedicalData):
    def accept(self, visitor):
        visitor.visit_medical_history(self)
        
        
# Visitor Interface
class MedicalVisitor(ABC):
    @abstractmethod
    def visit_symptoms(self, symptoms):
        pass
    
    @abstractmethod
    def visit_test_results(self, test_results):
        pass
    
    @abstractmethod
    def visit_medical_history(self, medical_history):
        pass
    
    
# Concrete Visitor: Medical Analysis
class DataAnalyzer(MedicalVisitor):
    def visit_symptoms(self, symptoms):
        print("Analyzing symptoms...")
        
    def visit_test_results(self, test_results):
        print("Analyzing test results...")
        
    def visit_medical_history(self,medical_history):
        print("Analyzing medical history...")
        
        
# Concrete Visitor: Diagnostic
class Diagnoser(MedicalVisitor):
    def visit_symptoms(self, symptoms):
        print("Diagnosing symptoms...")
        
    def visit_test_results(self, results):
        print("Diagnosing test results...")
        
    def visit_medical_history(self,medical_history):
        print("Diagnosing medical history...")
        
# Concrete Visitor: Patient Record Processing
class RecordProcessor(MedicalVisitor):
    def visit_symptoms(self, symptoms):
        print("Processing symptoms...")
        
    def visit_test_results(self, results):
        print("Processing test results...")
        
    def visit_medical_history(self, medical_history):
        print("Processing medical history...")
        

# Client code:
if __name__ == '__main__':
    medical_system = MedicalInformationSystem()
    
    # Add medical data to the system
    symptoms = Symptoms()
    test_results = TestResults()
    medical_history = MedicalHistory()
    
    medical_system.add_medical_data(symptoms)
    medical_system.add_medical_data(test_results)
    medical_system.add_medical_data(medical_history)
    
    # Process data using visitors
    analyzer = DataAnalyzer()
    medical_system.process_data(analyzer)
    
    diagnoser = Diagnoser()
    medical_system.process_data(diagnoser)
    
    record_processor = RecordProcessor()
    medical_system.process_data(record_processor)