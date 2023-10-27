from ninja import NinjaAPI
from ninja_extra import NinjaExtraAPI, api_controller, http_get, http_post, http_patch
from django.shortcuts import get_object_or_404
from .models import User
from .schema.response import (CustomerSchema, ErrorMsg, ConfirmationResponse, 
                            UserTokenResponse, UserTokenObtainSchema)
from .schema.payload import CustomerRegisterRequest
from typing import List
from ninja.responses import codes_4xx
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTAuth


from ninja_jwt.schema_control import SchemaControl
from ninja_jwt.settings import api_settings

api = NinjaExtraAPI()

schema = SchemaControl(api_settings)

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

@api_controller('/customer', tags=['Customer'])
class CustomerAPI:
    
    @http_get('/', response=CustomerSchema, auth=JWTAuth())
    def get_customer(self, request):
        return request.user
    
    @http_post('/register', response={401: ErrorMsg, 200:ConfirmationResponse})
    def register_customer(self, request, payload: CustomerRegisterRequest):
        if User.customers.filter(username=payload.username).exists():
            return 401, {'msg': 'Username already existed'}
        created_user = User.objects.create_user(**payload.dict())
        return 200, {'status':True, 'msg': ""}

    @http_post('/login', response=UserTokenResponse)
    def login_customer(self, user_token: UserTokenObtainSchema):
        user_token.check_user_authentication_rule()
        print(user_token.check_for_manager_role())
        return user_token.output_schema()
    

api.register_controllers(
    CustomerAPI,
    NinjaJWTDefaultController
)