from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from models.schema import AuthorsSchema 
from models.models import Authors
from db import get_db
import crud

authors_router = APIRouter()

@authors_router.post('/add-authors')
def add_authors(req: AuthorsSchema, db: Session = Depends(get_db)):
    try:
        result = crud.create_authors(req, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong!')


@authors_router.get('/get-authors')
def get_authors(db: Session = Depends(get_db)):
    try:
        result = crud.create_authors(db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong!')
    