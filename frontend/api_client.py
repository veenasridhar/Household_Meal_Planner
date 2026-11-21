import requests
from backend import models
from utils.log_setup import logger

base_url = 'http://127.0.0.1:8000'

def get_ingredients_list():
    response = requests.get(f"{base_url}/ingredients_list")
    if response.status_code == 200:
        ingredient_list = response.json()
    else:
        ingredient_list = []
    return ingredient_list


def save_recipe(recipe_data:models.Recipe):
    logger.info('From API Client Recipe Data:{}',recipe_data)
    '''POST endpoint to add the recipe model and ingredients model.'''
    response = requests.post(f'{base_url}/add_recipe',json= recipe_data)
    return response