from abc import ABC, abstractmethod

class CourseUpdate(ABC):
    
    @abstractmethod
    def update(self, id: int , name: str, description: str) -> dict:
        pass