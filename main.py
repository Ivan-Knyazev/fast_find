from database import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, APIRouter
# from fastapi.responses import JSONResponse, FileResponse
from typing import List
from find import *

app = FastAPI()

find_router = APIRouter(
    prefix="",
    tags=["Find User"]
)


@find_router.get("/api/users/find", response_model=List[UserSchema])
def get_user(required_user: str, db: Session = Depends(get_db)):
    users = db.query(User).all()
    return find_user(required_user, users)


@find_router.get("/api/users", response_model=List[UserSchema])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


app.include_router(find_router)

# @app.get("/api/users/{id}")
# def get_person(id, db: Session = Depends(get_db)):
#     # получаем пользователя по id
#     person = db.query(Person).filter(Person.id == id).first()
#     # если не найден, отправляем статусный код и сообщение об ошибке
#     if person == None:
#         return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
#     # если пользователь найден, отправляем его
#     return person
#
#
# @app.post("/api/users")
# def create_person(data=Body(), db: Session = Depends(get_db)):
#     person = Person(name=data["name"], age=data["age"])
#     db.add(person)
#     db.commit()
#     db.refresh(person)
#     return person
#
#
# @app.put("/api/users")
# def edit_person(data=Body(), db: Session = Depends(get_db)):
#     # получаем пользователя по id
#     person = db.query(Person).filter(Person.id == data["id"]).first()
#     # если не найден, отправляем статусный код и сообщение об ошибке
#     if person == None:
#         return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
#     # если пользователь найден, изменяем его данные и отправляем обратно клиенту
#     person.age = data["age"]
#     person.name = data["name"]
#     db.commit()  # сохраняем изменения
#     db.refresh(person)
#     return person
#
#
# @app.delete("/api/users/{id}")
# def delete_person(id, db: Session = Depends(get_db)):
#     # получаем пользователя по id
#     person = db.query(Person).filter(Person.id == id).first()
#
#     # если не найден, отправляем статусный код и сообщение об ошибке
#     if person == None:
#         return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
#
#     # если пользователь найден, удаляем его
#     db.delete(person)  # удаляем объект
#     db.commit()  # сохраняем изменения
#     return person
