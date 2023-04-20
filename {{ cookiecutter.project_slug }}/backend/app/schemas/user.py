from pydantic import BaseModel
from typing import Optional

# Shared properties
class UserBase(BaseModel):
    username: Optional[str] = None
    is_active: Optional[bool] = True
    access_level: int = 0
    full_name: Optional[str] = None

# Properties to receive via API on creation
class UserCreate(UserBase):
    username: str
    password: str

class User(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

# Properties to receive via API on update
class UserUpdate(BaseModel):
    password: Optional[str] = None
    is_active: Optional[bool] = None
    access_level: Optional[int] = None
    full_name: Optional[str] = None

class ChangePassword(BaseModel):
    password: str