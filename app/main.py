import asyncio
from database import AsyncSessionLocal, engine, Base
from crud.users import (
    create_user,
    get_user_with_posts,
    update_user_age,
    delete_user,
)
from crud.posts import create_post
from schemas import UserCreate, PostCreate

# ----- create Pydantic objects before main -----
user_in = UserCreate(name="Alice", age=25)
post_in = PostCreate(title="Hello", content="My first post")

async def main():
    # ----- create tables -----
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # ----- create user -----
    async with AsyncSessionLocal() as session:
        user = await create_user(session, user_in)
    # session closed

    # ----- create post -----
    async with AsyncSessionLocal() as session:
        post = await create_post(session, post_in, user.id)
    # session closed

    # ----- read user with posts -----
    async with AsyncSessionLocal() as session:
        data = await get_user_with_posts(session, user.id)
        print("User with posts:", data)

    # ----- update user age -----
    async with AsyncSessionLocal() as session:
        updated = await update_user_age(session, user.id, 30)
        print("Updated age:", updated.age)

    # ----- delete user -----
    async with AsyncSessionLocal() as session:
        await delete_user(session, user.id)

asyncio.run(main())
