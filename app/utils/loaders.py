from sqlalchemy import select
from sqlalchemy.orm import selectinload
from models import User

def user_with_posts(user_id: int):
    return (
        select(User)
        .where(User.id == user_id)
        .options(selectinload(User.posts))
    )
