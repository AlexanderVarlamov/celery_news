"""
version 
@author varlamov.a
@email varlamov.a@rt.ru
@date 30.11.2023
@time 10:17
"""
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from controllers.req_processors import get_json
from database.connections import get_async_session
from celery_apps.celery_app import periodical_insert
from database.db_actions import insert_news, get_number

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)

@router.post("/manual_update")
async def update_newslink():
    res = periodical_insert.delay()
    return res.get()


@router.post("/get_number")
async def update_newslink():
    # res = periodical_insert.delay()
    # return res.get()
    result = await get_number()
    return result
