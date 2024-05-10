from abc import ABC , abstractmethod

class Language(ABC):
    @abstractmethod
    def greet(self) -> str:
        pass
    