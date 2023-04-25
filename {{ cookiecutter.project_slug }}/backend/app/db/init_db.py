from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.enums import AccessLevel

def init_db(db:Session) -> None:
    user = crud.user.get_by_username(db, username='admin')
    if not user:
        user_in = schemas.UserCreate(
            username="{{cookiecutter.first_superuser}}",
            is_active=True,
            access_level=AccessLevel.SUPERUSER.value,
            full_name="{{cookiecutter.first_superuser}}",
            password="{{cookiecutter.first_superuser_password}}",
        )
        user = crud.user.create(db, obj_in=user_in)
    