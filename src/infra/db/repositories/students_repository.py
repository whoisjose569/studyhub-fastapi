from typing import Optional
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.students import Students as StudentsEntity
from src.data.interfaces.student_repository import StudentsRepositoryInterface
from src.domain.models.students import Students
from sqlalchemy import or_

class StudentsRepository(StudentsRepositoryInterface):
    
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
    def select_student(cls, search: str = '') -> list[Students]:
        with DBConnectionHandler() as database:
            try:
                students_on_db = database.db_session.query(StudentsEntity).filter(or_(StudentsEntity.name.ilike(f'%{search}%'),StudentsEntity.email.ilike(f'%{search}%'))).all()
                return students_on_db
            except Exception as exception:
                database.db_session.rollback()
                raise exception
    
    @classmethod
    def select_student_by_id(cls, id: int) -> Optional[Students]:
        with DBConnectionHandler() as database:
            try:
                student = database.db_session.query(StudentsEntity).filter_by(id=id).first()
                return student
            except Exception as exception:
                database.db_session.rollback()
                raise exception
    
    @classmethod
    def delete_student(cls, id: int) -> None:
        with DBConnectionHandler() as database:
            try:
                student = database.db_session.query(StudentsEntity).filter_by(id=id).first()
                database.db_session.delete(student)
                database.db_session.commit()
            except Exception as exception:
                database.db_session.rollback()
                raise exception
    
    @classmethod
    def update_student(cls, id: int, email: str) -> None:
        with DBConnectionHandler() as database:
            try:
                student = database.db_session.query(StudentsEntity).filter_by(id=id).first()
                student.email = email
                database.db_session.commit()
            except Exception as exception:
                database.db_session.rollback()
                raise exception