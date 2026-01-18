from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

async def raw_count_users(session: AsyncSession):
    result = await session.execute(text("SELECT COUNT(*) FROM users"))
    return result.scalar()
