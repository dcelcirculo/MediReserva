from pydantic import BaseModel, ConfigDict, EmailStr

class CreateUser(BaseModel):
    name: str
    email: EmailStr
    password: str
    rol: str = "patient"

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    rol: str

    model_config = ConfigDict(from_attributes=True)