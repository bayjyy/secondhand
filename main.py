from fastapi import FastAPI
from db import Base, engine
from routers import category_router, book_router, authors_router, authentication_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(category_router, tags=['Category'])
app.include_router(book_router, tags=['Book'])
app.include_router(authors_router, tags=['Authors'])
app.include_router(authentication_router, tags=['Authentication'])