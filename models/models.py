from datetime import datetime 
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey 
from sqlalchemy.orm import relationship
from db import Base

class Category(Base):
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True, index=True)
    name_tm = Column(String, nullable=False)
    name_ru = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


    Book = relationship('Book', back_populates='Category')

class Book(Base):
    __tablename__ = 'Book'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description_tm = Column(String, nullable=False)
    description_ru = Column(String, nullable=False)
    description_eng = Column(String, nullable=False)
    description_tr = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('Category.id'))
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    Category = relationship('Category', back_populates='Book')

    Authors = relationship('Authors', back_populates='Book')


class Authors(Base):
    __tablename__ = 'Authors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Integer, nullable=False)
    surname = Column(Integer, nullable=False)
    book_id = Column(Integer, ForeignKey("Book.id"))
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    Book = relationship('Book', back_populates='Authors')


class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    username = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
