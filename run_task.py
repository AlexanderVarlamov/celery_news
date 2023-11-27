"""
version 
@author varlamov.a
@email varlamov.a@rt.ru
@date 24.11.2023
@time 14:04
"""
from celery_test import test

print("start")
test.delay("hello")
print("finish")
