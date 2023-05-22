from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from models.schema import BookSchema
from models.models import Book
from db import get_db
import crud

book_router = APIRouter()

@book_router.post('/add-book')
def add_book(req: BookSchema, db: Session = Depends(get_db)):
    try:
        result = crud.create_book(req, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong!')

@book_router.get('/get-book')
def get_book(db: Session = Depends(get_db)):
    try:
        result = jsonable_encoder(crud.read_book(db))
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong!')


@book_router.get('/search')
def search(q: str, db: Session = Depends(get_db)):
    try:
        result = crud.search(q, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong!')


