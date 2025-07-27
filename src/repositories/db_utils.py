from .db_config import database_config
import gridfs


client, db, collection = database_config("local")

grid_fs = gridfs.GridFS(db)

def insert_file(file_object):

    _id = grid_fs.put(file_object, filename="file")
    print(grid_fs.get(_id))

    return _id

