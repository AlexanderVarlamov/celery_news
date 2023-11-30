"""
version 
@author varlamov.a
@email varlamov.a@rt.ru
@date 27.11.2023
@time 16:53
"""
import json
from asyncio import sleep
from datetime import datetime
from typing import List, Dict

from aiocache import cached, Cache
from sqlalchemy import select, insert

from database.connections import async_session_maker
from models.models import RssSource, NewsLinks


@cached(ttl=10, cache=Cache.MEMORY)
async def get_sources_from_db() -> List[RssSource]:
    async with async_session_maker() as session:
        query = select(RssSource).where(RssSource.is_active)
        result = await session.execute(query)
        return list(result.scalars())


@cached(ttl=10, cache=Cache.MEMORY)
async def get_number():
    import random as r
    number = r.randint(0, 100)
    await sleep(5)
    return number


async def insert_news(news_dict: Dict):
    async with async_session_maker() as session:
        links = json.dumps(news_dict, ensure_ascii=False)
        stmt = insert(NewsLinks).values(dt=datetime.utcnow(), links=links)
        await session.execute(stmt)
        await session.commit()


async def get_news():
    async with async_session_maker() as session:
        stmt = select(NewsLinks).limit(1)
        result = await session.scalars(stmt)
        res0 = next(result)
        print(type(res0.links))
        et = json.loads(res0.links)
        print(type(et))

# asyncio.run(get_news())
