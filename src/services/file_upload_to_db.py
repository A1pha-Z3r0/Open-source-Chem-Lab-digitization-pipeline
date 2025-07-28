"""
Has the service layer logic to put the incoming file into the db while creating a unique hashfile
to check duplicates
"""
from fastapi import UploadFile, HTTPException
from repositories.db_utils import insert_file
from ocr_pipeline import ocr_workflow
from .task import add
import hashlib


async def file_uploader(file: UploadFile):
    """
    Handles file upload, performs validation, and stores it in the database with a unique hash.

    Steps:
    - Validates MIME type (supports JPEG, PNG, PDF)
    - Ensures the file is non-empty
    - Computes SHA-256 hash to detect duplicates
    - Calls `insert_file` to store the binary in MongoDB
    - Triggers a background task for post-upload processing

    Args:
        file (UploadFile): File-like object received via FastAPI form upload

    Raises:
        HTTPException: 400 if the file is unsupported or empty
        HTTPException: 500 if DB insertion fails

    Returns:
        dict: JSON response with status message and inserted document ID
    """

    # store MIME content type & file name
    file_type = file.content_type
    file_name = file.filename

    # Read the file like objects contents
    contents = await file.read()

    # Create hash to keep track of unique entries
    file_hash = hashlib.sha256(contents).hexdigest()

    # Check if file is supported 
    if file_type not in ["image/jpeg", "image/png", "image/jpeg", "application/pdf"]:
        raise HTTPException(status_code=400, detail="File not supported")

    # Check if file is empty
    if not contents:
        raise HTTPException(status_code=400, detail="Empty file uploaded")

    try:
        _id = insert_file(file_object = contents,
                            hash_code = file_hash,
                            file_type = file_type,
                            file_name = file_name)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail= f"Error{e}")
    
    # Trigger a event based response to process the db content.
    ocr_workflow.delay()

    return {"message": "File uploaded successfully", "id": str(_id) }


