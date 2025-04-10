from fastapi import APIRouter
from controllers.UserController import getAllUsers,addUser,deleteUser,getUserById,loginUser
from models.UserModel import User,UserOut,UserLogin

router = APIRouter()

@router.get("/users/")
async def get_users():
    return await getAllUsers()

@router.post("/user/")
async def post_user(user:User):
    return await addUser(user)

@router.delete("/user/{userId}")
async def delete_user(userId:str):
    return await deleteUser(userId)

@router.get("/user/{userId}")
async def get_user_byId(userId:str):
    return await getUserById(userId)

@router.post("/user/login/")
async def login_user(user:UserLogin):
    return await loginUser(user)