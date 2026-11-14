from sqlmodel import SQLModel, Field, Text

class UserModel(SQLModel, table=True):
    id:int = Field(default=None, primary_key=True)
    name:str
    dietary_restrictions:str


class RecipeModel(SQLModel, table=True):
    id:int =Field(default=None,primary_key=True)
    user_id:int = Field(foreign_key="usermodel.id")
    name:str
    cooking_instructions:str | None = Field(default=None, sa_type=Text)   #sa_type is used to specify the underlying SQL type for the column, in this case, Text is used to store longer text data. 
    meal_type:str
    cooking_time:str
    serving_size:int

class IngredientModel(SQLModel, table=True):
    id:int = Field(default=None, primary_key=True)
    recipe_id:int = Field(foreign_key="recipemodel.id")
    name:str
    quantity:float
    unit:str

    