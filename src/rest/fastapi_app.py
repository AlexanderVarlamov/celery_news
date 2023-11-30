"""
version 
@author varlamov.a
@email varlamov.a@rt.ru
@date 30.11.2023
@time 10:02
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from .routers import router as operation_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(
    title="News App",
    lifespan=lifespan
)

app.include_router(operation_router)
