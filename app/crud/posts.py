from sqlalchemy.ext.asyncio import AsyncSession
from models import Post
from schemas import PostCreate

async def create_post(session: AsyncSession, post_in: PostCreate, user_id: int):
    post = Post(title=post_in.title, content=post_in.content, user_id=user_id)
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post
