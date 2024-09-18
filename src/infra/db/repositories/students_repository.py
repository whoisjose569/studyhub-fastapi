from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.students import Students as StudentsEntity

class StudentsRepository:
    
    @classmethod
    def insert_student(cls, name: str, email: str) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = StudentsEntity(name=name, email=email)
                database.db_session.add(new_registry)
                database.db_session.commit()
            except Exception as exception:
                database.db_session.rollback()
                raise exception