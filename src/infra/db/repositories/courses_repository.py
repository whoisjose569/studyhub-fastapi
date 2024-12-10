from typing import Optional
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.course import Course as CourseEntity
from src.data.interfaces.course_repository import CourseRepositoryInterface
from src.domain.models.courses import Courses

class CourseRepository(CourseRepositoryInterface):
    
    @classmethod
    def insert_course(self, name, description, start_date) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = CourseEntity(name = name, description = description , start_date = start_date)
                database.db_session.add(new_registry)
                database.db_session.commit()        
            except Exception as exception:
                database.db_session.rollback()
                raise exception
    
    @classmethod    
    def select_course(self, search = '') -> list[Courses]:
        with DBConnectionHandler() as database:
            try:
                course_on_db = database.db_session.query(CourseEntity).filter(CourseEntity.name.ilike(f"%{search}%")).all()
                return course_on_db
            except Exception as exception:
                database.db_session.rollback()
                raise exception
    
    @classmethod
    def select_course_by_id(self, id) -> Optional[Courses]:
        with DBConnectionHandler() as database:
            try:
                course_on_db = database.db_session.query(CourseEntity).filter_by(id=id).first()
                return course_on_db
            except Exception as exception:
                database.db_session.rollback()
                raise exception
    
    @classmethod     
    def delete_course(self, id) -> None:
        with DBConnectionHandler() as database:
            try:
                course_on_db = database.db_session.query(CourseEntity).filter_by(id=id).first()
                database.db_session.delete(course_on_db)
                database.db_session.commit()
            except Exception as exception:
                database.db_session.rollback()
                raise exception
    
    @classmethod
    def update_course(self, id, name, description) -> None:
        with DBConnectionHandler() as database:
            try:
                course_on_db = database.db_session.query(CourseEntity).filter_by(id=id).first()
                course_on_db.name = name
                course_on_db.description = description
                database.db_session.commit()
            except Exception as exception:
                database.db_session.rollback()
                raise exception