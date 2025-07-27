"""
Has the service layer logic to put the incoming file into the db while creating a unique hashfile
"""
from fastapi import UploadFile, HTTPException
from repositories.db_utils import insert_file
import hashlib



async def file_uploader(file: UploadFile):
    contents = await file.read()

    file_hash = hashlib.sha256(contents).hexdigest()

    if not contents:
        raise HTTPException(status_code=400, detail="Empty file uploaded")

    try:
        _id = insert_file(contents, file_hash)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail= f"Error{e}")


    return {"message": "File uploaded successfully", "id": str(_id) }


