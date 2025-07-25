"""
This has all the modules for reading a folder / database and pass it on to ocr
"""

import numpy as np

# pathlib is more OOP than os
from pathlib import Path

from utils import ImgConvertToTensor


class FileHandler():
    def __init__(self):
        self.list_img_np_array = []
        self.batch = None

    def files_to_tensor(self, path):
        
        # Img to tensor class instantiation
        # Define your folder path
        _path = Path(path)
        converter = ImgConvertToTensor()

        try:
            # check if file is supported
            if _path.suffix in [".png", ".jpeg", ".jpg", ".pdf"]:   
                #Helper from util thats called to make into tensor
                if _path.suffix == ".pdf":
                    tensor = converter.pdf_to_numpy(_path)
                    self.batch = np.stack(tensor, axis = 0)
                
                else:
                    tensor = converter.img_to_numpy(_path)
                    self.list_img_np_array.append(tensor)
                    self.batch = np.stack(self.list_img_np_array, axis = 0)

                self.list_img_np_array = []
                print(f"batch shape: {self.batch.shape}")

                return self.batch
            
            # Loop over all entries in a dir
            for entry in _path.iterdir():
                # Check if the type is an image
                if entry.suffix in [".png", ".jpeg", ".jpg"]:
                    print(entry.name)
                    # Convert image to tensor
                    tensors = converter.img_to_numpy(entry)

                    self.list_img_np_array.append(tensors)

                    # To debug
                    print(f"To debug: {tensors.shape}")

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
