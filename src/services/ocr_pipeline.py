from services.files_reader import FileHandler
from services.ocr import Ocr
import ray
import redis 

redis_client = redis.Redis(
    host="localhost", port=6379, db=0, decode_responses=True
)

ray.init()  

last_id = redis_client.get("ocr_last_id") or "0"


while True:
    msgs = redis_client.xread({"ocr_stream": last_id}, block=0)
    for _, entries in msgs:
        for message_id, data in entries:
            if data.get("event") == "files_ready":
                handler = FileHandler()

                batch_tensors = handler.files_to_tensor()

                ocr = Ocr.remote()

                ocr.full_ocr_pipeline.remote(batch_tensors)
                
                last_id = message_id
                redis_client.set("ocr_last_id", last_id)


   

