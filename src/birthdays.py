from celery import Celery
from time import sleep
import os
#celery -A birthdays worker --pool=solo --loglevel=info      рабочие процессы
#celery -A birthdays beat -l info                            планировщик ритмов

app = Celery(
    'birthdays', 
    broker = 'redis://redis:6379/0'
    )

app.conf.update(
    result_backend = 'redis://redis:6379/0'
    )

@app.task
def hello_world():
    return 'hello world matherfucker!'

@app.task
def add_digit(x, y):
    return x + y

@app.task
def send_row4pause(row, pause):
    sleep(pause)
    return "hello " + row