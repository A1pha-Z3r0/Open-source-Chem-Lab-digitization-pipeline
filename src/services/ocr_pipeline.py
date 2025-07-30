from .files_reader import FileHandler
from .ocr import Ocr
from celery_app import app

def get_FileHandler():
    if not FileHandler():
        handler = FileHandler
        return handler
    return None

# we call this every 5 mins
@app.task(queue = "processing")
def ocr_workflow():
    # initialize file handler class
    handler = get_FileHandler()

    list_ids = handler.db_to_tmps()
    print(f"The number of files present: {len(list_ids)}")

    # pass the directory with files
    batch_tensors = handler.files_to_tensor()
    
    # initialize ocr class
    ocr = Ocr()
    
    # text detection
    #ocr.text_detection("./test/f0072_36.png")
    
    # run the pipeline
    ocr.full_ocr_pipeline(batch_tensors)