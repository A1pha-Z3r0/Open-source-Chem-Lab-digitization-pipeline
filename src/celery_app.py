from celery import Celery

app = Celery(
    "ocr_pipeline",
    broker="pyamqp://guest:guest@localhost:5672/",  # RabbitMQ
    #backend="rpc://",  # or use Redis/MongoDB/Postgres for result backend
)

# Automatically discover all tasks from submodules
app.autodiscover_tasks([ "services", "repositories"])
