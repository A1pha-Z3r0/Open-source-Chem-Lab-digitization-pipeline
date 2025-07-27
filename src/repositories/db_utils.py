from .db_config import database_config
import gridfs


client, db, collection = database_config("local")

grid_fs = gridfs.GridFS(db)

def insert_file(file_object, hash):
    
    existing_file = grid_fs.find_one({"metadata.sha256": hash})
    if existing_file:
        return existing_file._id

    _id = grid_fs.put(file_object, filename="file", metadata={"sha256":hash})

    print(grid_fs.get(_id))

    return _id