""" 
This script has all the db related utils
"""

from .db_config import database_config
import gridfs


# returning the local / cloud client, db, collection
client, db, collection = database_config("local")

grid_fs = gridfs.GridFS(db)

db.fs.files.create_index("metadata.text_extraction_status")

def insert_file(file_object, hash_code, file_type, file_name):
    
    existing_file = grid_fs.find_one({"metadata.sha256": hash_code})
    if existing_file:
        return existing_file._id
    
    # take only the main extension
    file_type = file_type.split("/")[-1]
    
    metadata = {
        "shah": hash_code,
        "MIME_file_type":file_type,
        "text_extraction_status" : "Not Started"
    }

    _id = grid_fs.put(file_object, filename=file_name, metadata=metadata)

    print(grid_fs.get(_id))

    return _id

def list_not_started_files():
    list_ids = []

    for grid_out in grid_fs.find({"metadata.text_extraction_status": "Not Started"},
                        no_cursor_timeout=True):

        # Get id
        file_id = grid_out._id

        # get file name
        file_name = grid_out.filename

        #file_name = grid_out.filename

        #file_extension = grid_out.filename.rsplit(".")[1]

        # declare temps folder and format of file name
        temps_folder = f"../../temps/{file_id}_{file_name}"


        try:
            db.fs.files.update_one(
            {"_id": file_id},
            {"$set": {"metadata.text_extraction_status": "In Process"}})
            
            # write each grid_out data to its original file format in temps; the file name format is: file_id_file_name
            with open (temps_folder, "wb") as f:
                f.write(grid_out.read())

        except Exception as e:
            db.fs.files.update_one(
            {"_id": file_id},
            {"$set": {"metadata.text_extraction_status": "Not Started"}})


            print(f"Error Occrured: {e}")
            raise e

    
        list_ids.append(file_id)

    # return file paths and file_id (file_id to update it whenevr it finished)
    return list_ids

