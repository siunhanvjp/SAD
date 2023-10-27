from ninja import Schema

class CustomerRegisterRequest(Schema):
    username: str
    password: str
    email: str
    name: str = None
    phone_number: str = None
    
