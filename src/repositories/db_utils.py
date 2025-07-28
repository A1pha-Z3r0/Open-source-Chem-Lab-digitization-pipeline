from .db_config import database_config
import gridfs

client, db, collection = database_config("local")

grid_fs = gridfs.GridFS(db)

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
    for grid_out in grid_fs.find({"filename": "file"},
                        no_cursor_timeout=True):
    
        data = grid_out.read()

    return data

print(list_files())