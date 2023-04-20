from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import models
from app.db.session import engine
from app.routers import login, root, user
from app.routers.dependencies import get_current_active_user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    login.router,
    prefix="",
    tags=["Login"],
    responses={418: {"description": "I'm a teapot"}}
)

app.include_router(
    root.router,
    prefix="",
    tags=["Root"],
    dependencies=[Depends(get_current_active_user)],
    responses={418: {"description": "I'm a teapot"}}
)

app.include_router(
    user.router,
    prefix="/user",
    tags=["User"],
    dependencies=[Depends(get_current_active_user)],
    responses={418: {"description": "I'm a teapot"}}
)