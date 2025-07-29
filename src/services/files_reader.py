"""
This has all the modules for reading a folder / database and pass it on to ocr
"""

import numpy as np


# pathlib is more OOP than os
#from pathlib import Path

from utils import ImgConvertToTensor

from repositories.db_utils import list_files

class FileHandler():
    def __init__(self):
        self.list_img_np_array = []
        self.batch = None
        self.temps = "../../temps"


    def db_to_tmps():
        ids_list = list_files()

        return
    





    

    def files_to_tensor(self, file, file_type):
        

        # Define your folder path
        #_path = Path(path)
        # Img to tensor class instantiation
        converter = ImgConvertToTensor()

        try:
            # check if file is supported
            if file_type in [".png", ".jpeg", ".jpg", ".pdf"]:   
                #Helper from util called to make into tensor
                if file_type.suffix == ".pdf":
                    tensor = converter.pdf_to_numpy(file_type)  # SHAPE: [H, W, C]

                    # Batch it for better processing
                    self.batch = np.stack(tensor, axis = 0) # SHAPE: [batch, H, W, C]
                
                else:
                    tensor = converter.img_to_numpy(file_type)# SHAPE: [H, W, C]
                    self.list_img_np_array.append(tensor)
                    # Batch it for better processing
                    self.batch = np.stack(self.list_img_np_array, axis = 0)

                # Empty list to free space
                self.list_img_np_array = []
                print(f"TO DEBUG: batch shape: {self.batch.shape}")
                return self.batch
            
            """# Loop over all entries in a dir
            for entry in file_type.iterdir():
                # Check if the type is an image
                if entry.suffix in [".png", ".jpeg", ".jpg"]:
                    print(entry.name)
                    # Convert image to tensor
                    tensors = converter.img_to_numpy(entry)

                    self.list_img_np_array.append(tensors)

                    # To debug
                    print(f"To debug: {tensors.shape}")"""

            # Batch together images to create a single tensor
            self.batch = np.stack(self.list_img_np_array, axis = 0)
            # Make sure that the attribute is 0 to prevent data leaking
            self.list_img_np_array = []
            # To debug
            print(f"To debug: Passing this onto ocr as a batch: {self.batch.shape}")

            return self.batch
            

        except Exception as e:
            print(f"Error bhaiya1: {e}")
            return None


