from alembic.command import upgrade
from sqlmodel import SQLModel, Field, create_engine, Session
import psycopg2
from models import *
import sqlalchemy as sa

#creates a SQLAlchemy database engine using psycopg2.
engine = create_engine("postgresql+psycopg2://postgres:admin@localhost:5432/meal_planner", 
                       echo=True )

def create_tables(engine):
    SQLModel.metadata.create_all(engine)

def insert_rows(rows,engine=engine):
    with Session(engine) as session:
        for row in rows:
            session.add(row)
        session.commit()

#create_tables(engine)

