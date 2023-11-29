"""
version 
@author varlamov.a
@email varlamov.a@rt.ru
@date 27.11.2023
@time 15:20
"""
from typing import AsyncGenerator

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from config import *

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL, echo=True, poolclass=NullPool)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, )


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

