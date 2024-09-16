from decouple import config
from sqlalchemy import create_engine

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = config('DB_URL')
        self.__engine = self.__create_database_engine()
        
    
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine