from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database.create_db import Base
from datetime import datetime

class Data(Base):
    __tablename__ = 'some_table'


    id = Column(Integer, autoincrement=True, primary_key=True)
    some_str = Column(String)
    date_time = Column(DateTime, default=datetime.utcnow())


    def __init__(self, 
                 some_str: String, 
                 date_time: DateTime=None):
        

        self.some_str = some_str
        self.date_time = date_time





