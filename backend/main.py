from fastapi import FastAPI
from backend.router import recipe
from utils.log_setup import logger


app = FastAPI()

app. include_router(recipe.router,prefix = '', tags=['Recipe'])

base_url = 'http://localhost:8000'

@app.get('/')
async def root():
    logger.info('Logging Started')
    #add_users()
    return {"message": "Hello World"}

