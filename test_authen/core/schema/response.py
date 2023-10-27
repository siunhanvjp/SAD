from ninja import Schema, ModelSchema
from ..models import User
from typing import Any
from ninja_jwt.schema import TokenObtainPairInputSchema


class CustomerSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ['uuid', 'username', 'email', 'name', 'phone_number']
        
class ErrorMsg(Schema):
    msg: str

class ConfirmationResponse(Schema):
    status: bool
    msg: str

class UserTokenResponse(Schema):
    refresh: str
    access: str
    user: CustomerSchema

class UserTokenObtainSchema(TokenObtainPairInputSchema):

    def check_for_manager_role(self):
        return self._user.role == "M"

    def output_schema(self):
        out_dict = self.dict(exclude={"password"})
        out_dict.update(user=CustomerSchema.from_orm(self._user))
        return UserTokenResponse(**out_dict)

