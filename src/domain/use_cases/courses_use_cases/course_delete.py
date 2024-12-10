from abc import ABC, abstractmethod

class CourseDelete(ABC):
    
    @abstractmethod
    def delete(self, id: int) -> dict:
        pass