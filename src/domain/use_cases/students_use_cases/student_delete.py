from abc import ABC, abstractmethod

class StudentDelete(ABC):
    
    @abstractmethod
    def delete(self, id: int) -> dict:
        pass