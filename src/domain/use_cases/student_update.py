from abc import ABC, abstractmethod

class StudentUpdater(ABC):
    
    @abstractmethod
    def update(self, id: int, email: str) -> dict:
        pass