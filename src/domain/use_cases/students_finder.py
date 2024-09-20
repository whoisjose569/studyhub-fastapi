from abc import ABC, abstractmethod

class UserFinder(ABC):
    
    @abstractmethod
    def find(self, search: str) -> dict:
        pass