from ninja import Schema, ModelSchema
from ..models import User
from typing import Any

class UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ['username', 'email', 'role']
        
class ErrorMsg(Schema):
    msg: Any