from abc import ABC, abstractmethod

class StudentFinder(ABC):
    
    @abstractmethod
    def find(self, search: str) -> dict:
        pass