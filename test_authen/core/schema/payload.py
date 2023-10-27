from ninja import Schema

class UserRegisterRequest(Schema):
    username: str
    password: str
    email: str
    name: str = None
    phone_number: str = None
    
