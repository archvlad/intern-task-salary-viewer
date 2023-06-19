from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from passlib.context import CryptContext
import mysql.connector
import jwt
import datetime
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = FastAPI(title='Зарплата')

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class UserRegister(BaseModel):
    username: str
    password: str


class User(BaseModel):
    user_id: str


PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return PWD_CONTEXT.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return PWD_CONTEXT.hash(password)


@app.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="root", database="salary_viewer_db")
    mycursor = mydb.cursor()

    username = form_data.username
    password = form_data.password

    mycursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    myresult = mycursor.fetchall()
    if len(myresult) == 0 or not verify_password(password, myresult[0][2]):
        raise HTTPException(
            status_code=400, detail='Incorrect username or password')
    lifetime = datetime.timedelta(minutes=float(
        os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES')))
    exp = datetime.datetime.now(datetime.timezone.utc) + lifetime
    access_token = jwt.encode(
        {'user': myresult[0][0], 'exp': exp}, os.environ.get('ACCESS_TOKEN_SECRET'), 'HS256')

    return {"access_token": access_token}


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, os.environ.get(
            'ACCESS_TOKEN_SECRET'), ['HS256'])
    except jwt.exceptions.InvalidSignatureError:
        raise HTTPException(
            status_code=401, detail="JWT token has invalid signature")
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="JWT token expired")
    return payload


@app.get('/me')
def me(user: User = Depends(get_current_user)):
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="root", database="salary_viewer_db")
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM users WHERE user_id = %s', (user['user'],))
    myresult = mycursor.fetchall()
    about_me = {'user_id': myresult[0][0], 'username': myresult[0][1]}
    mycursor.execute(
        'SELECT * FROM salaries WHERE user_id = %s', (user['user'],))
    myresult = mycursor.fetchall()
    about_me['salary'] = myresult[0][1]
    mycursor.execute(
        'SELECT * FROM next_increases WHERE user_id = %s', (user['user'],))
    myresult = mycursor.fetchall()
    about_me['next_increase'] = myresult[0][1]
    return about_me
