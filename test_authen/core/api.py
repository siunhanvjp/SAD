from ninja import NinjaAPI
from ninja_extra import NinjaExtraAPI, api_controller, http_get, http_post, http_patch
from django.shortcuts import get_object_or_404
from .models import User
from .schema.response import UserSchema, ErrorMsg
from .schema.payload import UserRegisterRequest
from typing import List
from ninja.responses import codes_4xx
from ninja_jwt.controller import NinjaJWTDefaultController

api = NinjaExtraAPI()

# @api.get("/user/{pk}", response={200: UserSchema, 405: ErrorMsg})
# def view_user(request, pk):
#     try:
#         return 200, User.objects.get(pk=pk)
#     except Exception as err:
#         return 405, {'msg': err}

# @api.post("/user", response={codes_4xx: ErrorMsg})
# def register_user(request, payload: UserRegisterRequest):
#     if User.customers.filter(email=payload.email).exists():
#         return 405, {"msg": "Email already exists"}
#     created_user = User.objects.create_user(**payload.dict())
#     return True

# @api.post('/login')
# def login_user(request, payload: UserSchema):
#     pass

# register(give information -> return confirmation ), 
# login(give username, passwor -> return jwt), 
# profile(give jwt -> get info)

@api_controller('/user', tags=['Customer'])
class CustomerAPI:
    
    @http_get('/{user_id}', response=UserSchema)
    def get_customer(self, request, user_id: str):
        return User.objects.get(pk=user_id)
    
api.register_controllers(
    CustomerAPI,
    NinjaJWTDefaultController
)