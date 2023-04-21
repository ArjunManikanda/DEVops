from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel


app = FastAPI()

security = HTTPBasic()

users = {
    1:{
    'name':'test1',
    'age':'22',
    'class':'python',
    'username':'user1',
    'password':'pass1'
    },
    2:{
    'name':'test2',
    'age':'33',
    'class':'fastapi',
    'username':'user2',
    'password':'pass2'
    },
    3:{
    'name':'test3',
    'age':'44',
    'class':'javascript',
    'username':'user3',
    'password':'pass3'
    },
    4:{
    'name':'vasanth',
    'age':'34',
    'class':'Devops',
    'username':'user4',
    'password':'pass4'
    }

}


class User(BaseModel):
    name: str
    age: int
    class_: str
    username: str
    password: str


@app.get("/")
async def root():
    return {"message": "my first api"}


#### get every users by name ####
@app.get("/get-users")
def get_user(name : str):
    for i in users:
        if users[i]['name'] == name:
            return users[i]
    return {'user':'not found'}


#### delete user ####
@app.delete("/delete-users")
def del_user(user_id : int):
    for id in users.keys():
        if id == user_id:
            del users[id]
            return {'id': user_id}
    return {'id':'does not match'}


@app.get("/get-users/{user_id}")
def userdata(user_id:int):
    return users[user_id]


@app.get("/get-user-by-name")
def getting_users(name:str):
    for user in users:
        if user['name'] == name:
            return user
    return {'data':'not found'}


@app.put("/add_user")
def ad_user(user: User):
    users[len(users) + 1] = user.dict()


@app.post("/login")
def login(credentials: HTTPBasicCredentials = Depends(security)):
    for user in users.values():
        if user['username'] == credentials.username and user['password'] == credentials.password:
            return {"status": "Login Successful"}
    raise HTTPException(status_code=401, detail="Incorrect username or password")
