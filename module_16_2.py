from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})

#app = FastAPI()

# импорт класс FastAPI

#app = FastAPI()
#приложение(объект) FastAPI

@app.get("/")
async def main_page() -> dict:
    #Создание маршрута к главной странице - "/".
    # По нему должно выводиться сообщение "Главная страница".
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def admin_page() -> dict:
    #Создание маршрута к странице админа - "user/admin".
    # По нему должно выводиться сообщение "Вы вошли как администратор".
    return {"message": "Вы вошли как администратор"}

#description="The ID must be a positive integer",
@app.get('/user/{user_id}')
async def get_user_id(
user_id: Annotated[int, Path(ge=1, le=100,description="Enter user ID", example='1')]
) -> dict:
    # Создание маршрута к страницам пользователей - '/user/{user_id}'.
    # По нему должно выводиться сообщение "Вы вошли как пользователь".
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user/{username}/{age}')
async def get_user_info(
username: Annotated[str, Path(min_length=5, max_length=20,description="Enter Username",
pattern="^[A-Za-z\\s]+$",example="Vladis")],
age:Annotated[int, Path(ge=18, le=120,description="Enter age",example="57")]
)-> dict:
    #маршрут к страницам пользователей передавая данные  в адресной строке - "/user"
    return {'message':
            f'Информация о пользователе. Имя: {username}, Возраст: {age}'}