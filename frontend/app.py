import streamlit as st

st.set_page_config(layout="wide")
with st.sidebar:
    st.title('Meal Planner')
    plan_meal_page = st.Page('plan_meals.py', title = 'Plan your meals')
    recipe_page = st.Page('recipe_editor.py', title = 'Recipe Editor')
    pg = st.navigation([plan_meal_page, recipe_page])

pg.run()

