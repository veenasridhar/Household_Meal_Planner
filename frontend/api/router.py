from fastapi import APIRouter
import requests

router = APIRouter()
base_url = 'http://0.0.0.0:8000'

def get_ingredients_list():

    response = requests.get(f"{base_url}/ingredients_list")
    if response.status_code == 200:
        return response.json().get("ingredients", [])
    else:
        return []

def save_receipe(recipe_data):
    '''POST endpoint to add the recipe model and ingredients model.'''
    response = requests.post(f'{base_url}/add_recipe',json=recipe_data)
    return response