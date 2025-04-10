from pydantic import BaseModel,Field,validator
from bson import ObjectId
import bcrypt
from typing import Optional, Dict, Any


class User(BaseModel):
    firstName:str
    lastName:str
    age:int
    status:bool
    role_id:str
    email:str
    password:str

    @validator("password",pre=True,always=True)
    def encrypt_password(cls,v):
        if v is None:
            return None
        return bcrypt.hashpw(v.encode("utf-8"),bcrypt.gensalt())

class UserOut(User):
    id:str = Field(alias="_id")
    role:Optional[Dict[str,Any]] = None
    email:Optional[str] = None
    password:Optional[str] = None

    @validator("id",pre=True,always=True)
    def convert_objectId(cls,v):
        if isinstance(v,ObjectId):
            return str(v)
        return v

    @validator("role", pre=True, always=True)
    def convert_role(cls,v):
        if isinstance(v, dict) and "_id" in v:
            v["_id"] = str(v["_id"])
        return v
    
class UserLogin(BaseModel):
    email:str
    password:str