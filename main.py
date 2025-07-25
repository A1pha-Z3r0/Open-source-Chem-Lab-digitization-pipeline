"""
This script has the main python functions
"""

from src.files_reader import FileHandler
from src.ocr import Ocr

def main():
    # initialize file handler class
    handler = FileHandler()

    # pass the directory with files
    batch = handler.files_to_tensor("./test/f0072_36.png")
    
    # initialize ocr class
    ocr = Ocr()
    
    # text detection
    ocr.text_detection("./test/f0072_36.png")    

    quit()
    
    # run the pipeline
    ocr.full_ocr_pipeline(batch)
    
    


if __name__ == "__main__":
    main()