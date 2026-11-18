from fastapi import FastAPI
from backend.db import insert_rows,create_tables
from backend.models import *

app = FastAPI()


base_url = 'http://localhost:8000'

@app.get('/')
async def root():
    #add_users()
    return {"message": "Hello World"}

def add_users():
    user1 = user(name="Veena", dietary_restrictions="Vegetarian")
    insert_rows([user1])

@app.post("/add_recipe")
async def add_recipe(recipe_data):
    # Example of adding a recipe to the database
    new_recipe = recipe(name=recipe_data['name'],
        cooking_instructions=recipe_data['cooking_instructions'],
        meal_type=recipe_data['meal_type'],
        cooking_time=recipe_data['cooking_time'],
        serving_size= recipe_data['serving_size']
    )
    insert_rows([new_recipe])
    print('The id is generated:', new_recipe.id)

    for ingred in recipe_data['ingredients_dict']:
        curr_ingredient = ingredient(
            name=ingred['name'],
        )
        insert_rows([curr_ingredient])
        print('The ingredient id is generated:', curr_ingredient.id)

    return {"message": "Recipe added successfully"}

@app.get(f"/ingredients_list")
async def get_ingredients_list():
    # Example of retrieving the ingredients list for a specific user
    ingredients = get_ingredients_list()
    return {"ingredients": ingredients}