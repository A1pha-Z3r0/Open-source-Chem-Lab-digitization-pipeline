"""
This script has the main python functions
"""
from fastapi import FastAPI
from api import file_upload_routes

app = FastAPI()

app.include_router(file_upload_routes.router, prefix = "/files")




"""
from services.files_reader import FileHandler
from services.ocr import Ocr

def main():
    # initialize file handler class
    handler = FileHandler()

    # pass the directory with files
    batch_tensors = handler.files_to_tensor("../test/f0072_36.png")
    
    # initialize ocr class
    ocr = Ocr()
    
    # text detection
    #ocr.text_detection("./test/f0072_36.png")
    
    # run the pipeline
    ocr.full_ocr_pipeline(batch_tensors)
    
    


if __name__ == "__main__":
    main()

"""