"""
This is a utility script runs the OCR pipeline and output texts.
Input: images/pdfs
Output: text
"""
import torch
from doctr.io import read_img_as_tensor, read_img_as_numpy, read_pdf

# batch processing

class ImgConvertToTensor():
    def __init__(self):
        pass
    def img_to_tensor(self,path):
        page = read_img_as_tensor(path, dtype = torch.uint8)
        return page
    def img_to_numpy(self, path):
        page = read_img_as_numpy(path)
        return page
    def pdf_to_numpy(self,path):
        page = read_pdf(path)
        return page
  

    
# for real time explore
# doctr.io.decode_img_as_tensor()