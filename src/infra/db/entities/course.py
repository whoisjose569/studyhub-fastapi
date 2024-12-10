from sqlalchemy import Column, String, Integer, DateTime
from src.infra.db.settings.base import Base

class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    
    def __repr__(self):
        return f"Course [id={self.id}, name={self.name}]"