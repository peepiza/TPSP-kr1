from fastapi.responses import HTMLResponse
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import User
from models_new import User1
from models_new import Feedback
from models_3 import Feedback3
from models_3 import User3

ap = FastAPI()

#1.1
@ap.get("/first")
def root():
    return {"message": "Авторелоад действительно работает"}
#1.2
@ap.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)
#1.3
class Numbers(BaseModel):
    num1: float
    num2: float

@ap.post("/calculate")
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result", result}
#1.4
my_user = User(name="Вероника Дмитриева", id=1)

@ap.get("/user")
async def get_user():
    return my_user

#1.5
'''def check_is_adult(age: int) -> bool:
    return age >= 18

@ap.post("/user1")
async def create_user(user: User1):
    is_adult = check_is_adult(user.age)

    user_data = {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }
    return user_data'''

#2.1
'''feedback_storage = []

@ap.post("/user1")
async def create_user(user: User1):
    return {
        "name": user.name,
        "age": user.age,
    }
@ap.post("/feedback")
async def create_feedback(feedback: Feedback):
    feedback_storage.append(feedback)

    return {
        "message": f"Feedback received. Thank you, {feedback.name}."
    }
@ap.get("/feedback")
async def get_all_feedback():
    return {"feedback": feedback_storage}

@ap.get("/users")
async def get_user():
    return {"name": "Ваше Имя Фамилия", "id": 1}'''


#2.2
feedback_storage_sec = []

@ap.post("/user3")
async def create_user(user: User3):
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": user.age >= 18
    }

@ap.post("/feedback3")
async def create_feedback(feedback: Feedback3):
    feedback_storage_sec.append(feedback)

    return {
        "message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."
    }

@ap.get("/feedback3")
async def get_all_feedback():
    return {"feedbacks": feedback_storage_sec}

@ap.get("/user4")
async def get_user():
    return {"name": "Иван Петров", "id": 1}