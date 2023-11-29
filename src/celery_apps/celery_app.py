"""
version 
@author varlamov.a
@email varlamov.a@rt.ru
@date 24.11.2023
@time 10:30
"""
import asyncio

from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger

from controllers.req_processors import get_json
from database.db_actions import insert_news

logger = get_task_logger(__name__)
celery_app = Celery("celery_app",
                    broker='redis://127.0.0.1:6379',
                    backend='redis://127.0.0.1:6379',
                    )


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/20'), periodical_insert, name="Читаем новости и пишем их в базу")


async def insert_to_base():
    result = await get_json()
    await insert_news(result)


@celery_app.task
def periodical_insert():
    import platform
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(insert_to_base())
