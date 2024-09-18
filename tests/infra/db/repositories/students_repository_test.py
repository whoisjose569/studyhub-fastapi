from src.infra.db.entities.students import Students as StudentsEntity
from src.infra.db.repositories.students_repository import StudentsRepository

def test_insert_student(db_session):
        try:
            name = 'Jose'
            email = 'test@test'
            students_repository = StudentsRepository()
            students_repository.insert_student(name, email)
            
            student_on_db = db_session.query(StudentsEntity).filter_by(name=name).first()
            
            assert student_on_db is not None
            assert student_on_db.name == name
            assert student_on_db.email == email
            
            db_session.delete(student_on_db)
            db_session.commit()
        
        except Exception as exception:
            db_session.rollback()
            raise exception