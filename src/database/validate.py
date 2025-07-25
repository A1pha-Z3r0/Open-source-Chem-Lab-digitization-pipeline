"""
This script has a type checker using pydantic for the required fields.
"""

from pydantic import BaseModel, field_validator
import numpy as np

class data_valid(BaseModel):
    doc_type : str # the type of input doc
    file : object # the actual file
    ocr_tensors : np.ndarray # input tensors
    output_text = str # predicted output


    # decorator to check custom types and conditionals
    @field_validator("ocr_tensors", mode="before") #@field_validator("the_respective_field_to_check", mode="before")
    @classmethod # pydantic requires it to be classmethod
    def convert_to_numpy(cls, v):
        # convert to np.array
        arr = np.array(v)

        if arr.dtype != np.uint8:
            raise ValueError("Expected a uint8 array")
        
        return arr


    @field_validator("ocr_tensors")
    @classmethod
    def check_shape(cls, arr):
        if arr.ndim != 3:
            raise ValueError("Expected a 3D array")
        return arr


