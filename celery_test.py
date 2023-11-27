"""
version 
@author varlamov.a
@email varlamov.a@rt.ru
@date 24.11.2023
@time 10:30
"""
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger
import random as r

logger = get_task_logger(__name__)
celery_app = Celery("test_app",
                    broker='redis://127.0.0.1:6379',
                    backend='redis://127.0.0.1:6379',
                    # broker='redis://127.0.0.1:6379'
                    )


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # # Calls test('hello') every 10 seconds.cele
    # sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')
    #
    # # Calls test('hello') every 30 seconds.
    # # It uses the same signature of previous task, an explicit name is
    # # defined to avoid this task replacing the previous one defined.
    # sender.add_periodic_task(30.0, test.s('hello'), name='add every 30')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(timedelta(milliseconds=1), add, name="Складываем два числа")



    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )


@celery_app.task
def test(arg):
    logger.info("Hi!")
    logger.info(arg)
    print(arg)


@celery_app.task
def add():
    x, y = r.randint(1, 15), r.randint(2, 100)
    z = x + y
    logger.info(f"{x} {y}")
    logger.info(z)
