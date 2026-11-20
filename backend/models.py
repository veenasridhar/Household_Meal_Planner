
from __future__ import annotations                              #To look into the future for the definitions
from sqlmodel import SQLModel, Field, Text, Relationship
from pydantic import BaseModel, field_validator, FieldValidationInfo
from backend.schemas import *
import re
import unicodedata
from utils.log_setup import logger

# class user(SQLModel, table=True):
#     id:int = Field(default=None, primary_key=True)
#     name:str
#     dietary_restrictions:str

# class recipe(SQLModel, table=True):
#     id:int | None =Field(default=None,primary_key=True)
#     user_id:int = Field(foreign_key="user.id",index=True)
#     name:str 
#     cooking_instructions:str | None = Field(default=None, sa_type=Text)   #sa_type is used to specify the underlying SQL type for the column, in this case, Text is used to store longer text data. 
#     meal_type:str
#     cooking_time:str
#     serving_size:int
#     recipe_ingredients: list['recipeingredient'] = Relationship(back_populates ='recipe')

# class ingredient(SQLModel, table=True):
#     id:int | None = Field(default=None, primary_key=True)
#     name:str
#     recipe: list['recipeingredient'] = Relationship(back_populates = 'ingredient') 

# class recipeingredient():
#     id: int | None = Field(default=None,primary_key=True)
#     recipe_id:int = Field(default=None,foreign_key='recipe.id',index=True)
#     ingredient_id:int = Field(default=None, foreign_key='ingredient.id',index=True)
#     quantity:float
#     unit:str
#     recipes: recipe = Relationship(back_populates = 'recipeingredient')
#     ingredients: ingredient = Relationship(back_populates = 'recipeingredient')

class user(BaseModel):
    id:int
    name:str
    dietary_restrictions:str

class Ingredients(BaseModel):
    ingredient_id: int | None=Field(default=None, description='Id Primary key')
    ingredient_name:str
    quantity:float
    unit:str

class Recipe(BaseModel):
    recipe_id:int | None =Field(default=None, description='Id Primary key')
    user_id:int = Field(nullable=False, description='User Id Foreign Key')
    recipe_name:str = Field(description='Recipe Name')
    cooking_instructions:str | None = Field(default='',description='Cooking instructions') 
    cooking_time:str = Field(description='30 mins')
    serving_size:int = Field(description='Serving size')
    meal_type:str = Field(description = 'Meal Type')
    recipe_ingredients: list[Ingredients]
    
    @field_validator('recipe_name', 'cooking_instructions', 'cooking_time', 'meal_type', mode='before') # use '*' to select all fields
    @classmethod    #Python decorator that makes a method belong to the class rather than an individual object (instance).
    def clean_text(cls, input_text:str, info:FieldValidationInfo) -> str:
        '''Function cleans the text, becuase sometimes input copy pasted from websites which might have  spurious characters.
        First, Normalize the unicode characters (if any) into same way.'''

        logger.info('{} field validation started', info.field_name)
        
        input_text = unicodedata.normalize('NFC',input_text)

        # Replace common unusual spaces
        input_text = re.sub(r'[\u00A0\u1680\u2000-\u200A\u202F\u205F\u3000]', ' ', input_text)

        # Remove unwanted ASCII control characters
        input_text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F\xa0]', '', input_text)

        # Remove common invisible characters
        input_text = re.sub(r'[\u200B\uFEFF]', '', input_text)

        return input_text.strip()

class RecipeIngredient(BaseModel):
    id:int|None
    recipe_id:int
    ingredient_id:int
    quantity:float|None
    unit:str|None












    