
from datetime import date
from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    full_name: str
    date_of_birth: Optional[date] = None
    sex: Optional[str] = None
    email: EmailStr
    password: str
    pin_code: Optional[str] = None
    address: Optional[str] = None
    blood_group: Optional[str] = None
    phone: Optional[str] = None


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    blood_group: Optional[str] = None

    class Config:
        from_attributes = True
