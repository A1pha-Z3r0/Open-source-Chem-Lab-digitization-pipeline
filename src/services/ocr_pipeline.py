from .files_reader import FileHandler
from .ocr import Ocr
import torch
#from repositories.db_utils import write_notStarted_to_temps()

#_handler = None  # private module-level cache

# Periodically call this; and only call inference "when the load is enough"
def get_FileHandler():
    global _handler
    if _handler is None:
        _handler = FileHandler()
    return _handler

#app.task(queue = "file handler", name = "" )
#async def write_to_temps():
#    list_ids = write_notStarted_to_temps()

# we call this every 5 mins
def ocr_workflow():
    # initialize file handler class
    print("hello Im running")

    device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')

    handler = FileHandler()

    list_ids = handler.db_to_tmps()

    print(f"The number of files present: {len(list_ids)}")

    # pass the directory with files
    batch_tensors = handler.files_to_tensor()
    
    # initialize ocr class
    ocr = Ocr(device)
    
    # text detection
    #ocr.text_detection("./test/f0072_36.png")
    
    # run the pipeline
    ocr.full_ocr_pipeline(batch_tensors)