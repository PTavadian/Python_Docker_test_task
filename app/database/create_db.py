from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2


DATABASE_NAME = 'test_db'

engine = create_engine(f"postgresql+psycopg2://admin:root@db_some:5437/{DATABASE_NAME}", echo=True)


Session = sessionmaker(bind=engine) 

Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)

