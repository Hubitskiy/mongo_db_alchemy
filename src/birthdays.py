from celery import Celery
from time import sleep
from random import shuffle
import os


app = Celery(
    'birthdays', 
    #broker = 'redis://redis:6379/0',
    #backend = 'redis://redis:6379/0'
    broker = 'amqp://rabbitmq:rabbitmq@rabbit:5672',
    backend = 'amqp://rabbitmq:rabbitmq@rabbit:5672'
    )


@app.task
def hello_world():
    return 'hello world mather!'

@app.task
def add_digit(x, y):
    return x + y

@app.task
def send_row4pause(row, pause):
    sleep(pause)
    return "hello " + row

@app.task
def my_sort(x):
	arr = list(range(10 ** x))
	shuffle(arr)
	sorted(arr)
	return 'done'