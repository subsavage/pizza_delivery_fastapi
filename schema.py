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

class Settings(BaseModel):
    authjwt_secret_key:str='f3682e152ccf17e4ff2b246bb28a8c8e0f37b483c1d5b0dcc9bbe549d5968d72'

class LoginModel(BaseModel):
    username:str
    password:str

class OrderModel(BaseModel):
    id:Optional[int]
    quantity:int
    order_status:Optional[str]="PENDING"
    pizza_size:Optional[str]="SMALL"
    user_id:Optional[int]

    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                "quantity":2,
                "pizza_size":"LARGE"
            }
        }