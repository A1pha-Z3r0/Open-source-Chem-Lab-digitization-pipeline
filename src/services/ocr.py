"""
This script has the ocr pipeline
"""

import torch 
#import matplotlib.pyplot as plt

from doctr.models import ocr_predictor

#from doctr.utils.visualization import visualize_page
from utils import ImagePreprocess
import ray


#from ultralytics import YOLO
#from huggingface_hub import hf_hub_download
#from matplotlib import pyplot as plt


@ray.remote
class Ocr():
    def __init__(self):
        # to turn gpu in mac if accelerator is available
        self.device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
        self.model = ocr_predictor('linknet_resnet50', 'master', 
                                   pretrained= True ).to(self.device)

    def full_ocr_pipeline(self, batch):
        """
        This function runs the model and outputs the prediction.
        Params: np array of dim [batch, number of images, height, width, channel]
        output: str of prediction
        """
        preprocessor = ImagePreprocess()

        for _file_name, tensor_list in batch.items():

            if isinstance(tensor_list,list):
                
                print(f"To debug: {tensor_list.shape}")
                print(f"To debug: ")

                output = self.model(tensor_list)

                text_output = output.render()

            print(f"file name: {_file_name} \n predicted text: {text_output}")

        else:
            raise TypeError("Error bhaiya: The input tensors are not a list!") 

            #visualize_page(output.pages[0].export(), tensor_list)
            #plt.show()

        return text_output


