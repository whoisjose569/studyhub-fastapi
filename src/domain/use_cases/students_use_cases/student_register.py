from abc import ABC, abstractmethod

class StudentRegister(ABC):
    
    @abstractmethod
    def register(self, name: str, email: str) -> dict:
        pass