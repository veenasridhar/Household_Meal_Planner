from fastapi import APIRouter
from backend.models import *
from utils.log_setup import logger
from backend.db import *



router = APIRouter()

def add_users():
    user1 = user_schema(name="Veena", dietary_restrictions="Vegetarian")
    insert_rows([user1])


@router.post("/add_recipe")
def add_recipe(recipe_data:Recipe):
    # Example of adding a recipe to the database
    logger.info("Recipe Data: {}",recipe_data)

    with Session(engine) as session:

        new_recipe = Recipe_schema(
                user_id = recipe_data.user_id,
                name = recipe_data.recipe_name,
                cooking_instructions=recipe_data.cooking_instructions,
                meal_type = recipe_data.meal_type,
                cooking_time = recipe_data.cooking_time,
                serving_size = recipe_data.serving_size)

        for ingredient in recipe_data.recipe_ingredients:
        
            curr_ingredient = ingredient_schema(
                name=ingredient.ingredient_name,
            )

            recipe_ingredient = RecipeIngredient_schema(
                ingredient = curr_ingredient,
                quantity=ingredient.quantity,
                unit = ingredient.unit)
            new_recipe.recipe_ingredients.append(recipe_ingredient)

        session.add(new_recipe)
        session.commit()
    
        return {"message": "Recipe added successfully",
                "recipe_id":new_recipe.id}

@router.get(f"/ingredients_list")
def get_ingredients_list():
    # Example of retrieving the ingredients list for a specific user
    ingredients = get_ingredients_list()
    return {"ingredients": ingredients}

# def get_ingredients_list():
#     response = requests.get(f"{base_url}/ingredients_list")
#     if response.status_code == 200:
#         return response.json().get("ingredients", [])
#     else:
#         return []


# def save_receipe(recipe_data:Recipe):
#     logger.info('Recipe Data:',recipe_data)
#     '''POST endpoint to add the recipe model and ingredients model.'''
#     response = requests.post(f'{base_url}/add_recipe',recipe_data)
#     return response