
from sqlmodel import SQLModel, Field, Text, Relationship

class user(SQLModel, table=True):
    id:int = Field(default=None, primary_key=True)
    name:str
    dietary_restrictions:str

class recipe(SQLModel, table=True):
    id:int | None =Field(default=None,primary_key=True)
    user_id:int = Field(foreign_key="user.id",index=True)
    name:str 
    cooking_instructions:str | None = Field(default=None, sa_type=Text)   #sa_type is used to specify the underlying SQL type for the column, in this case, Text is used to store longer text data. 
    meal_type:str
    cooking_time:str
    serving_size:int
    recipe_ingredients: list['recipeingredient'] = Relationship(back_populates ='recipe')

class ingredient(SQLModel, table=True):
    id:int | None = Field(default=None, primary_key=True)
    name:str
    recipe: list['recipeingredient'] = Relationship(back_populates = 'ingredient') 

class recipeingredient():
    id: int | None = Field(default=None,primary_key=True)
    recipe_id:int = Field(default=None,foreign_key='recipe.id',index=True)
    ingredient_id:int = Field(default=None, foreign_key='ingredient.id',index=True)
    quantity:float
    unit:str
    recipes: recipe = Relationship(back_populates = 'recipeingredient')
    ingredients: ingredient = Relationship(back_populates = 'recipeingredient')



    