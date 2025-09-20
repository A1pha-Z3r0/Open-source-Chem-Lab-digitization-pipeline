from celery import Celery
from datetime import timedelta



app = Celery(
    "ocr_pipeline",
    broker="pyamqp://guest:guest@localhost:5672/",  # RabbitMQ
    backend="rpc://",  # or use Redis/MongoDB/Postgres for result backend
)

# Automatically discover all tasks from submodules
#app.autodiscover_tasks([ "services", "repositories"])


app.conf.beat_schedule = {
    'batch-every-5-mins': {
        'task': 'celery_tasks.get_write_to_temps',
        'schedule': timedelta(minutes=1),
    },
}

from services import celery_tasks


