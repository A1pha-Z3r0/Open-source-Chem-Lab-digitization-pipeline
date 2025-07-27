"""
This file consists routing for file upload
"""

from fastapi import APIRouter, HTTPException, status, UploadFile
from services.file_upload_to_db import file_uploader

router = APIRouter()

# Route file-upload calls the ocr processing
@router.post("/file-upload", status_code= status.HTTP_201_CREATED)
async def upload_file_to_db(file : UploadFile):
    """
    Uploads a file, stores it in the database, and returns its ID.

    Args:
        file (UploadFile): Supported formats: .png, .jpeg, .jpg, .pdf

    Raises:
        HTTPException: 400 - if file is empty
        HTTPException: 500 - if DB insertion fails

    Returns:
        dict: JSON response containing a success message and unique file ID
    """
    return await file_uploader(file)




 


