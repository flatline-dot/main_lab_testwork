import os
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from .models import Base

db_path = os.path.join('..', 'sqlite.db')

DATABASE_URL = f'sqlite+aiosqlite:///{db_path}'

engine = create_async_engine(DATABASE_URL)


async def create_db():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

if __name__ == '__main__':
    asyncio.run(create_db())