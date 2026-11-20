import streamlit as st
#from backend.api import router
from api_client import *

def add_ingredient(ingredient_name, quantity, unit):
    curr_ingredient = {
        'ingredient_name':ingredient_name,
        'quantity':quantity,
        'unit':unit
    }
    st.session_state.curr_ingredients_list.append(curr_ingredient)

def create_recipe():
    
    recipe_data = {
                    'user_id':1,            # TODO: Add user auth and use automatic user.id
                    'recipe_name' : st.session_state.recipe_name, 
                   'cooking_instructions' : st.session_state.cooking_instructions,
                    'meal_type' : st.session_state.meal_type, 
                    'cooking_time' :st.session_state.cooking_time, 
                    'serving_size' : st.session_state.serve_size,
                    'recipe_ingredients' : st.session_state.curr_ingredients_list
                    }
    save_recipe(recipe_data)


st.session_state.ingredient_list = []
st.session_state.curr_ingredients_list = []

col1, col2 = st.columns([1,7])

with col2:  
    with st.container(border = True):
        st.title('Recipe Editor')
        st.session_state.recipe_name = st.text_input('Enter recipe name')
        col3, col4, col5, col6 = st.columns([2,2,1,1])
        with col3:
            ingredient_name = st.selectbox('Select ingredients', st.session_state.ingredient_list, accept_new_options=True)
        with col4:
            quantity = st.text_input('Enter quantity')
        with col5:
            unit = st.selectbox('Select unit', ['grams', 'ml', 'cups', 'tablespoons', 'teaspoons', 'pieces'])
        with col6:
            st.write(' ')
            st.write(' ')
            st.button('Add Ingredient', on_click=add_ingredient(ingredient_name, quantity, unit))
        
        st.session_state.cooking_instructions = st.text_area('Enter cooking instructions')
        st.session_state.meal_type = st.selectbox('Select meal type', ['Breakfast', 'Lunch', 'Dinner', 'Snack', 'Soup', 'Salad', 'Dessert'])
        st.session_state.cooking_time = st.text_input('Enter cooking time (in minutes)')
        st.session_state.serve_size = st.number_input('Enter serving size', min_value=1, max_value=20, step=1)
        st.button('Save Recipe', on_click=create_recipe())

        
