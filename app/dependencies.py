from sqlalchemy.ext.asyncio import AsyncSession
from .create_db import engine


async def get_session():
    async with AsyncSession(engine) as session:
        yield session
