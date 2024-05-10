from international_factory import InternationalFactory
from spanish import Spanish
from Madrid import Madrid
from capital_city import CapitalCity
from language import Language

class SpainFactory(InternationalFactory):
    
    def create_language(self) -> Language:
        return Spanish()
    
    def create_capital(self) -> CapitalCity:
        return Madrid()
        