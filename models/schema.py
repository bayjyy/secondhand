from pydantic import BaseModel

class CategorySchema(BaseModel):
    name_tm = str 
    name_ru = str 

class BookSchema(BaseModel):
    name = str 
    description_tm = str 
    description_ru = str
    description_eng = str
    description_tr = str 
    category_id = int 

class AuthorsSchema(BaseModel):
    name = str 
    surname = str 
    book_id = int 
    
class loginSchema(BaseModel):
    email: str
    password: str 

class registerSchema(loginSchema):
    username: str 