from models.UserModel import User,UserOut,UserLogin
from bson import ObjectId
from config.database import user_collection,role_collection
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import bcrypt
from utils.SendMail import send_mail


async def addUser(user:User):
    user.role_id = ObjectId(user.role_id)
    print("after type cast",user.role_id)
    result = await user_collection.insert_one(user.dict())
    send_mail(user.email,"User Created","user created successfully ..!")
    # return {"message":"User Created Successfully!"}
    return JSONResponse(status_code =201,content={"message":"User Created Successfully!"})
# async def getAllUsers():
#     users = await user_collection.find().to_list()
#     print("users...",users)
#     return [UserOut(**user) for user in users]
# async def addUser(user:User):
#     result = await user_collection.insert_one(user.dict())
#     return{"message":"User create successfully..!"}

async def deleteUser(userId:str):
    result = await user_collection.delete_one({"_id":ObjectId(userId)})
    print("after delete result",result)
    return {"Message":"user Deleted Successfully!"}

async def getUserById(userId:str):
    result = await user_collection.find_one({"_id":ObjectId(userId)})
    print(result)        
    return UserOut(**result)

async def getAllUsers():
    users = await user_collection.find().to_list(length=None)

    for user in users:
            if "role_id" in user and isinstance(user["role_id"],ObjectId):
                    user["role_id"] = str(user["role_id"])

            role = await role_collection.find_one({"_id": ObjectId(user["role_id"])})

            if role:
                role["_id"] = str(role["_id"])
                user["role"] = role

    return [UserOut(**user) for user in users]
        
async def loginUser(request: UserLogin):
    foundUser = await user_collection.find_one({"email": request.email})
    print("found user",foundUser)
    foundUser["_id"] = str (foundUser["_id"])
    foundUser["role_id"] = str(foundUser["role_id"])

    if foundUser is None:
        raise HTTPException(status_code=404,detail="user not found")
    
# for compare password
    if "password" in foundUser and bcrypt.checkpw(request.password.encode(),foundUser["password"].encode()):
        role = await role_collection.find_one({"_id":ObjectId(foundUser["role_id"])})
        foundUser["role"] = role
        return{"message":"user login successfully..!","user":UserOut(**foundUser)}
    else:
        raise HTTPException(status_code=404,detail="Invalid password")