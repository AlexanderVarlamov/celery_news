"""
version 
@author varlamov.a
@email varlamov.a@rt.ru
@date 24.11.2023
@time 14:04
"""
from celery_apps.celery_app import periodical_insert

print("start")
res = periodical_insert.delay()
print(res.get())
print("finish")
