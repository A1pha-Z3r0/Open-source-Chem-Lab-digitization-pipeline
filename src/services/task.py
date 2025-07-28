from celery import Celery


app = Celery('task', 
             broker='pyamqp://guest:guest@localhost:5672/')
@app.task
def add(x,y):
    return x + y