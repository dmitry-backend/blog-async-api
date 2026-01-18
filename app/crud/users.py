from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession	# a class that allows session objs support and process in async funcs
from models import User
from schemas import UserCreate
from utils.loaders import user_with_posts

async def create_user(session: AsyncSession, user_in: UserCreate):
    user = User(name=user_in.name, age=user_in.age)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

async def get_user(session: AsyncSession, user_id: int):
    result = await session.execute(
        select(User).where(User.id == user_id)
    )
    return result.scalar_one_or_none()

async def get_user_with_posts(session: AsyncSession, user_id: int):
    result = await session.execute(
        user_with_posts(user_id)
    )
    return result.scalar_one_or_none()

async def update_user_age(session: AsyncSession, user_id: int, age: int):
    user = await session.get(User, user_id)
    if not user:
        return None
    user.age = age
    await session.commit()
    return user

async def delete_user(session: AsyncSession, user_id: int):
    user = await session.get(User, user_id)
    if not user:
        return False
    await session.delete(user)
    await session.commit()
    return True
