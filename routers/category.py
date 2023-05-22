from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.encoders import  jsonable_encoder
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from db import get_db 

import crud
from models.models import Category
from models.schema import CategorySchema

category_router = APIRouter()

@category_router.post('/add-category')
def add_category(req: CategorySchema, db: Session = Depends(get_db)):
    try:
        result = crud.create_category(req, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong!')


@category_router.get('/get-category')
def get_category(db: Session = Depends(get_db)):
    try:
        result = jsoanable_encoder(crud.read_category(db))
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong!')

