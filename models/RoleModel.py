from pydantic import BaseModel,Field,validator
from bson import ObjectId

#  _id:Field pk , ObjectId

class Role(BaseModel):
    name:str
    description:str

  # Response class
class RoleOut(Role):
    id:str = Field(alias="_id")

    @validator("id", pre=True, always=True)
    def convert_objectId(cls,v):
        if isinstance(v,ObjectId):
            return str(v)
        
        return v