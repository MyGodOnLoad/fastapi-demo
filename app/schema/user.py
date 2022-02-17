from pydantic import BaseModel


class UserBase(BaseModel):
    """用户基础类"""
    username: str
    email: str
    tel: str


class CreateUser(UserBase):
    """新建用户模型"""
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
