from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy import Text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class user_schema(Base):
    __tablename__ = 'user'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(30))
    dietary_restrictions:Mapped[str] = mapped_column(String(60))

class Ingredient(Base):
    __tablename__ = 'ingredient'
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str] =mapped_column(String(30))
    recipe_ingredients: Mapped[List['RecipeIngredient']] = relationship(
        back_populates='ingredient')
class RecipeIngredient(Base):
    __tablename__ = 'recipeingredient'
    id:Mapped[int]=mapped_column(primary_key=True)
    recipe_id:Mapped[int]=mapped_column(ForeignKey('recipe.id'))
    ingredient_id:Mapped[int] = mapped_column(ForeignKey('ingredient.id'))
    quantity:Mapped[Optional[float]]
    unit:Mapped[Optional[str]]
    recipe: Mapped['Recipe_schema'] = relationship(
        back_populates='recipe_ingredients'
    )

    ingredient: Mapped['Ingredient'] = relationship(
        back_populates='recipe_ingredients'
    )

class Recipe_schema(Base):
    __tablename__ = 'recipe'
    id: Mapped[Optional[int]] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey(user_schema.id))
    name:Mapped[str] = mapped_column(String(30))
    cooking_instructions:Mapped[str] = mapped_column(Text)
    meal_type:Mapped[str] = mapped_column(String(30))
    cooking_time:Mapped[str] = mapped_column(String(30))
    serving_size:Mapped[int] = mapped_column(Integer)
    recipe_ingredients: Mapped[List['RecipeIngredient']] = relationship(
        back_populates='recipe',
        cascade='all, delete-orphan'
    )

