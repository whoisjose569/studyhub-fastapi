from abc import ABC, abstractmethod

class StudentFinderById(ABC):
    
    @abstractmethod
    def find_by_id(self, id: int) -> dict:
        pass