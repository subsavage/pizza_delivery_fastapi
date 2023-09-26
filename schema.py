from pydantic import BaseModel
from sqlalchemy import Column,Integer,Boolean,Text,String,ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship
from typing import Optional


class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]
    
class Config:
    orm_mode=True
    schema_extra={
        'example':{
            "username":"harshit",
            "email":"harshit@gmail.com",
            "password":"pasword",
            "is_staff":False,
            "is_active":True
        }
    }