from pydantic import BaseModel

class _UserBase(BaseModel):
    username:str
    
    class Config:
        orm_mode = True

class userid(_UserBase):
    id:int

    class Config:
        orm_mode = True

class UserCreate(_UserBase):
    email : str
    password:str
    address : str
    age : int
    college_name : str

    class Config:
        orm_mode = True

class UserUpdate(_UserBase):
    email : str
    address : str
    age : int
    college_name : str

    class Config:
        orm_mode = True

class userpass(_UserBase):
    password:str
     
    class config:
        orm_mode = True
    
class TokenData(BaseModel):
    username:str

    class config:
        orm_mode = True
