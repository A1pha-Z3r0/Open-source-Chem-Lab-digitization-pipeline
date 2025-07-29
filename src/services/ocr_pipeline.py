from .files_reader import FileHandler
from .ocr import Ocr
from celery_app import app

@app.task
def ocr_workflow():
    # initialize file handler class
    handler = FileHandler()

    # pass the directory with files
    batch_tensors = handler.files_to_tensor(_file, _filetype)
    
    # initialize ocr class
    ocr = Ocr()
    
    # text detection
    #ocr.text_detection("./test/f0072_36.png")
    
    # run the pipeline
    ocr.full_ocr_pipeline(batch_tensors)