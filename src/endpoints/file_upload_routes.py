"""
This file consists routing for file upload
"""

from fastapi import APIRouter, HTTPException, status
from optical_character_rec.files_reader import FileHandler
from optical_character_rec.ocr import Ocr

router = APIRouter()
handler = FileHandler()
ocr = Ocr()

# Route file-upload calls the ocr processing
@router.post("/file-upload", status_code= status.HTTP_201_CREATED)
async def upload_file(file):
    """
    Processes a file into tensors and calls the ocr_processing to store the text


    Args:
        file (_type_): png, jpeg, jpg, pdf 

    Raises:
        HTTPException: 400; if file is empty 
        HTTPException: 500; if any unknown error

    Returns:
        HTTPS JSON object: if file upload successful a JSON with body text
    """

    try:
        batch_tensors = handler.files_to_tensor(file)

        if not batch_tensors:
            raise HTTPException(status_code=400, detail = "Empty file")

        ocr.full_ocr_pipeline(batch_tensors)

    except Exception as e:
        raise HTTPException(status_code=500, detail= f"Error{e}")


    return {"message": "File uploaded successfully"}




 


