from sqlmodel import SQLModel, Field, create_engine, Session, select
import psycopg2
import backend.models as models
import sqlalchemy as sa

#creates a SQLAlchemy database engine using psycopg2.
engine = create_engine("postgresql+psycopg2://postgres:admin@localhost:5432/meal_planner", 
                       echo=True )

def create_tables():
    SQLModel.metadata.create_all(engine)

def insert_rows(rows,engine=engine):
    with Session(engine) as session:
        for row in rows:
            session.add(row)
        session.commit()

def get_ingredients_list():
    with Session(engine) as session:
        statement = select(models.ingredient.name)
        result = session.exec(statement).all
        print('tHE RESULT IS',result)
        return result

#create_tables(engine)

