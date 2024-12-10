from abc import ABC, abstractmethod

class CourseFinder(ABC):
    
    @abstractmethod
    def find(self, search: str = '') -> dict:
        pass