from .db_config import database_config
import gridfs

client, db, collection = database_config("local")

grid_fs = gridfs.GridFS(db)

db.fs.files.create_index("metadata.text_extraction_status")

def insert_file(file_object, hash_code, file_type, file_name):
    
    existing_file = grid_fs.find_one({"metadata.sha256": hash_code})
    if existing_file:
        return existing_file._id
    
    metadata = {
        "shah": hash_code,
        "file_type":file_type,
        "text_extraction_status" : "Not Started"
    }

    _id = grid_fs.put(file_object, filename=file_name, metadata=metadata)

    print(grid_fs.get(_id))

    return _id

def list_files():
    list_ids = []

    for grid_out in grid_fs.find({"metadata.text_extraction_status": "Not Started"},
                        no_cursor_timeout=True):

        file_id = grid_out._id

        file_name = grid_out.filename

        temps_folder = f"../../temps/{file_id}/{file_name}"


        try:
            db.fs.files.update_one(
            {"_id": file_id},
            {"$set": {"metadata.text_extraction_status": "In Process"}})
            
            # write each grid_out data to its original file format in temps
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

print(list_files())