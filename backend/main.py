from fastapi import FastAPI
from db import insert_rows
from models import *

app = FastAPI()

@app.get("/")
async def root():
    #add_users()
    return {"message": "Hello World"}

def add_users():
    user1 = UserModel(name="Veena", dietary_restrictions="Vegetarian")
    insert_rows([user1])

@app.get("/add_recipe")
async def add_recipe():
    # Example of adding a recipe to the database
    new_recipe = RecipeModel(
        user_id=1,
        name="Minestrone Soup",
        cooking_instructions='''1.Heat the oil in a large saucepan or casserole pot over a low-medium heat and gently fry the onion, celery, carrot, courgette and pancetta for 10 mins. Add the garlic and oregano, and cook for 1 min. Tip in the beans, chopped tomatoes, purée, stock and bay leaf. Season to taste. Bring to the simmer and cook for 30 mins.
        2. Add the pasta and cook for 10 mins, or until tender. Stir in the spinach and cook for 1 min, or until wilted. Remove from the heat and stir in the parmesan. Serve with crusty bread.''',
        meal_type="Dinner,Soup",
        cooking_time=60.0,
        serving_size= 4
    )
    insert_rows([new_recipe])

    # ingredient1 = IngredientModel(
    #     recipe_id=new_recipe.id,
    #     name="Pasta",
    #     quantity=200.0
    # )

    
    return {"message": "Recipe added successfully"}