from pymongo import IndexModel, ASCENDING
from typing import Optional
from pydantic import Field, EmailStr
from app.core.eve_model import EveModel

# user_schema = {
#     'username': {'type': 'string', 'unique': True, 'minlength': 3, 'maxlength': 50},
#     'email': {'type': 'string', 'unique': True},
#     'age': {'type': 'integer', 'min': 18}
# }

class UserModel(EveModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    age: Optional[int] = Field(default=None, ge=18)
    password: str = Field(..., min_length=6)
    role: str = Field(default="user")
    token: str = Field(default="")


users = {
    'schema': UserModel.cerberus_schema(),
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'item_methods': ['GET', 'PATCH', 'DELETE'],
    'indexes': [IndexModel([("username", ASCENDING)], unique=True)],
    'projection': {
        "password": 0,
        "token": 0
    }
}
