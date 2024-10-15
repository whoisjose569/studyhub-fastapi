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

def test_select_student(db_session):
    try:
        student = StudentsEntity(name='Jose', email='test@test')
        db_session.add(student)
        db_session.commit()
        
        student_repository = StudentsRepository()
        students = student_repository.select_student()
        
        students_on_db = db_session.query(StudentsEntity).all()
        
        assert students_on_db[0].name == students[0].name
        assert students_on_db[0].email == students[0].email
        
        db_session.delete(student)
        db_session.commit()
             
    except Exception as exception:
            db_session.rollback()
            raise exception

def test_select_student_by_id(db_session):
    try:
        student = StudentsEntity(id=32, name='teste', email='teste2@teste.com')
        db_session.add(student)
        db_session.commit()
        
        student_repository = StudentsRepository()
        student_on_db = student_repository.select_student_by_id(32)
        
        assert student_on_db.id == student.id
        
        db_session.delete(student)
        db_session.commit()
    except Exception as exception:
        db_session.rollback()
        raise exception
        
        