from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any

from app import crud, schemas
from app.db import models
from app.routers.dependencies import get_db, get_current_active_user
from app.core.enums import AccessLevel

router = APIRouter()

@router.post("", response_model=schemas.User,)
def create_user(*,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_active_user),
        user_in: schemas.UserCreate
    ) -> Any:
    """
    Create new user.
    """
    if current_user.access_level != AccessLevel.SUPERUSER.value:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    user = crud.user.get_by_username(db, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    return crud.user.create(db, obj_in=user_in)

@router.get("")
async def get_users(*, db: Session = Depends(get_db)):
    users = crud.user.get_multi(db)
    for user in users:
        del user.hashed_password
    return users

@router.put("")
async def update_user(*,
    db: Session = Depends(get_db),
    user_id: int,
    user_in: schemas.UserUpdate,
    current_user: models.User = Depends(get_current_active_user)
) -> Any:
    if current_user.access_level != AccessLevel.SUPERUSER.value:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    return crud.user.update(db, db_obj=user, obj_in=user_in)

@router.patch("")
async def change_password(*,
    db: Session = Depends(get_db),
    user_in: schemas.ChangePassword,
    current_user: models.User = Depends(get_current_active_user)
) -> Any:
    user = crud.user.get(db, id=current_user.id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    return crud.user.update(db, db_obj=user, obj_in=user_in)

@router.delete("")
async def delete_user(*, id:int, db:Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    if current_user.access_level != AccessLevel.SUPERUSER.value:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return crud.user.remove(db,id=id)

