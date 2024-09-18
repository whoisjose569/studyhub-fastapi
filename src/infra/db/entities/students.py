from sqlalchemy import Column, String, Integer, DateTime, func
from src.infra.db.settings.base import Base

class Students(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    enrollment_date = Column(DateTime, server_default=func.now())
    
    def __repr__(self):
        return f"Students [id={self.id}, name={self.name}]"