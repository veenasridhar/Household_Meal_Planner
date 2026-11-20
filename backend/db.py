from sqlmodel import SQLModel, Field, create_engine, Session, select
import psycopg2
import backend.models as models
from backend.schemas import *
import sqlalchemy as sa
from utils.log_setup import logger

#creates a SQLAlchemy database engine using psycopg2.
engine = create_engine("postgresql+psycopg2://postgres:admin@localhost:5432/meal_planner", 
                       echo=True )

def create_tables():
    logger.info('Creating Tables')
    Base.metadata.create_all(engine)

def insert_rows(row,engine=engine):
    with Session(engine) as session:
        session.add(row)
        session.commit()
        session.refresh(row)
    return row.id

def get_ingredients_list():
    with Session(engine) as session:
        statement = select(models.ingredient.name)
        result = session.exec(statement).all
        logger.info('tHE RESULT IS {}',result)
        return result

create_tables()

