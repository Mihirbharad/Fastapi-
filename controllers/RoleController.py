from config.database import role_collection
from models.RoleModel import Role,RoleOut
from bson import ObjectId

async def getAllRoles():
     
    #  find ---> select * from roles
    roles = await role_collection.find().to_list()
    print("roles...",roles)
    return [RoleOut(**role) for role in roles]

async def addRole(role:Role):
    result = await role_collection.insert_one(role.dict())
    print(result)
    return{"message":"role create successfully"}
    
async def deleteRole(roleId:str):
    result = await role_collection.delete_one({"_id":ObjectId(roleId)})
    print("after delete result",result)
    return {"Message":"Role Deleted Successfully!"}


async def getRoleById(roleId:str):
    result = await role_collection.find_one({"_id":ObjectId(roleId)})
    print(result)        
    return RoleOut(**result)

    #return {"message":"role fetched successfully!"}
    #return result
