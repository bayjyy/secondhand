import sqlalchemy

from models import Category, Book, Authors
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func, or_

def create_category(req, db: Session):
    new_add = Category(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add 

def read_category(db: Session):
    result = db.query(Category).options(joinedload(Category.Book)).all()
    return result

def create_book(req, db: Session):
    new_add = Book(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add

def read_book(db: Session):
    result = db.query(Book).options(joinedload(Book)).join(Category, Category.Category_id == Book.Category_id).all()
    return result

def search(q, db: Session):
    result = db.query(Book)\
        .filter(
            or_(
                func.lower(Book.name_tm).like(f'%{q}%'),
                func.lower(Book.name_ru).like(f'%{q}%'),
            )
        ).all()
    return result


def signUp(req, db: Session):
    user = db.query(Users).filter(
        or_(
            Users.email == req.email,
            Users.username == req.username
        )
    ).first()
    if user:
        return False
    new_add = Users(**req.dic())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return True 


def signIn(req, db: Session):
    user = db.query(Users).filter(
        and_(
            or_(
                Users.email == req.email,
                Users.username == req.username
            ),
            Users.password == req.password
        )
    ).first()
    if user:
        return True 

def read_users(db: Session):
    return db.query(Users.id, Users.email, Users.username).all()