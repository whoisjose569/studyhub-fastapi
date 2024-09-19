from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.students import Students as StudentsEntity
from sqlalchemy import or_

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
    
    @classmethod
    def select_student(cls, search: str = '') -> any:
        with DBConnectionHandler() as database:
            try:
                students_on_db = database.db_session.query(StudentsEntity).filter(or_(StudentsEntity.name.ilike(f'%{search}%'),StudentsEntity.email.ilike(f'%{search}%'))).all()
                return students_on_db
            except Exception as exception:
                database.db_session.rollback()
                raise exception