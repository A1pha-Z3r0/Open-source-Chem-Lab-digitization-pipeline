"""
This has all the modules for reading a folder / database and pass it on to ocr
"""

import numpy as np

# pathlib is more OOP than os
from pathlib import Path
from utils import ImgConvertToTensor
from repositories.db_utils import list_not_started_files
from collections import OrderedDict


class FileHandler():
    def __init__(self):
        self.list_img_np_array = []
        self.batch = OrderedDict()
        self.temps_folder = "../../temps"


    def db_to_tmps():
        ids_list = list_not_started_files()
        return ids_list

    def files_to_tensor(self, ids_list, file_type):
        
        # Define your folder path
        _path = Path(self.temps_folder)
        # Img to tensor class instantiation
        converter = ImgConvertToTensor()
        """
        for file in list_of_files:
            extension = file.rsplit["."][-1]
            try:
                # check if file is supported
                if extension in [".png", ".jpeg", ".jpg", ".pdf"]:   
                    #Helper from util called to make into tensor
                    if extension == ".pdf":
                        tensor = converter.pdf_to_numpy(file)  # SHAPE: [H, W, C]

                        # Batch it for better processing
                        self.batch = np.stack(tensor, axis = 0) # SHAPE: [batch, H, W, C]
                    
                    else:
                        tensor = converter.img_to_numpy(file)# SHAPE: [H, W, C]
                        self.list_img_np_array.append(tensor)
                        # Batch it for better processing
                        self.batch = np.stack(self.list_img_np_array, axis = 0)

                    # Empty list to free space
                    self.list_img_np_array = []
                    print(f"TO DEBUG: batch shape: {self.batch.shape}")
                    return self.batch"""
                
        # Loop over all entries in a dir
        for entry in _path.iterdir():
            try:
                # Check if the type is an image
                if entry.suffix.lower() in [".png", ".jpeg", ".jpg"]:

                    print(f"To Debug: {entry.name}")
                    # Convert image to tensor

                    tensors = converter.img_to_numpy(entry) # SHAPE: [H, W, C]

                    self.batches[entry.name] = list(tensors)

                    # To debug
                    print(f"To debug: {tensors.shape}")

                elif entry.suffix.lower() in [".pdf"]:
                    tensors = converter.pdf_to_numpy(entry)  # a list of pages, each element having SHAPE: [H, W, C]

                    self.batches[entry.name] = tensors

                else:
                    raise TypeError("Unexpected file type")
            
            except Exception as e:
                print(f"Error bhaiya1: {e}")
                return None
        
        self.batch = np.stack(self.list_img_np_array, axis = 0) # SHAPE: [batch, H, W, C]

        # Make sure that the attribute is 0 to prevent data leaking
        self.list_img_np_array = []
        # To debug
        print(f"To debug: Passing this onto ocr as a batch: {self.batch.shape}")

        return self.batch
                

           


