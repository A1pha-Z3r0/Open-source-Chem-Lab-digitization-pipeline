from celery import Celery
from datetime import timedelta

app = Celery(
    "ocr_pipeline",
    broker="pyamqp://guest:guest@localhost:5672/",  # RabbitMQ
    #backend="rpc://",  # or use Redis/MongoDB/Postgres for result backend
)

# Automatically discover all tasks from submodules
app.autodiscover_tasks([ "services", "repositories"])


app = Celery("batch")
app.conf.beat_schedule = {
    'batch-every-10-seconds': {
        'task': 'services.ocr_pipeline',
        'schedule': timedelta(minutes=5),
    },
}