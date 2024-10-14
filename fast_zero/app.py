from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from http import HTTPStatus
from fast_zero.schemas import (
    Message, 
    UserDB,
    UserPublic,
    UserSchema, 
  )

app = FastAPI()
database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)  
def read_root():  
    return {'message': 'Olá Mundo!'}

@app.get('/challange', status_code=HTTPStatus.OK, response_class=HTMLResponse)  
def read_root_html():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""

@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_users(user: UserSchema):
    user_with_id = UserDB(
        id=len(database) + 1, 
        **user.model_dump()
    )

    database.append(user_with_id)

    return user_with_id
