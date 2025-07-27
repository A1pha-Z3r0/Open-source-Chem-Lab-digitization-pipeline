"""
This file consists routing for file upload
"""

from fastapi import APIRouter, HTTPException, status, UploadFile
from repositories.db_utils import insert_file

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
    contents = await file.read()

    if not contents:
        raise HTTPException(status_code=400, detail="Empty file uploaded")

    try:
        _id = insert_file(contents)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail= f"Error{e}")


    return {"message": "File uploaded successfully", "id": str(_id) }




 


