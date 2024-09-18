import pytest
from src.infra.db.settings.connection import DBConnectionHandler

@pytest.fixture
def db_session():
    with DBConnectionHandler() as database:
        yield database.db_session
        database.db_session.rollback()