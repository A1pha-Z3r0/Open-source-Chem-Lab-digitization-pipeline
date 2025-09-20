from repositories.db_utils import write_to_temps
from celery_app import app
import redis


# Periodically call this; and only call inference "when the load is enough"
@app.task(queue = "processing", name = "celery_tasks.get_write_to_temps")
def get_write_to_temps():
    """
    This function writes the files from db to temps folder for further processing
    Returns:
        list : a list of ids that have to be processed
    """
    print("Hello Im running")

    redis_client = redis.Redis(host="localhost", port=6379, db=0)

    list_ids = write_to_temps()

    print(f"The number of files present: {len(list_ids)}")

    threshold = 10

    #if len(list_ids) >= threshold:
    redis_client.xadd("ocr_stream", {"event": "files_ready"})
    print("Hey I wrote 1 'im ready' ")

    return list_ids

