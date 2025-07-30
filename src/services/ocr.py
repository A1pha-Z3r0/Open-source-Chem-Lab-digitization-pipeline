"""
This script has the ocr pipeline
"""

import torch 
import matplotlib.pyplot as plt

from doctr.models import ocr_predictor

from doctr.utils.visualization import visualize_page
from utils import ImagePreprocess

from ultralytics import YOLO
from huggingface_hub import hf_hub_download
from matplotlib import pyplot as plt


class Ocr():
    def __init__(self,):
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

                output = self.model(tensor_list)

                text_output = output.render()

            print(f"file name: {_file_name} \n predicted text: {text_output}")

            #visualize_page(output.pages[0].export(), tensor_list)
            #plt.show()

        return text_output

        """
            for i in range (0, len(tensor_list)):

                print(f"Image shape: {tensor_list[i].shape}")
                
            if isinstance(image,list):
                print(type(image))
                print(image.shape)
                
                image = preprocessor.normalize(image)

                output = self.model(image)

            else:
                image = preprocessor.normalize(image)

                image = preprocessor.thresholding(image)

                print(f"input shape after threshold: {image.shape}")
                print(f"TO DEBUG: data type of input: {image.dtype}")

                output = self.model([image])

            text_output = output.render()

            print(text_output)

            visualize_page(output.pages[0].export(), image)
            plt.show()

        return text_output"""

    def text_detection(self, img_path):
        # Load the weights from our repository
        model_path = hf_hub_download(local_dir="..",
                                     repo_id="armvectores/yolov8n_handwritten_text_detection",
                                     filename="../best.pt")
        model = YOLO(model_path)

        # Do the predictions
        res = model.predict(
            source=img_path, 
            project='.',
            name='detected', 
            exist_ok=True, 
            save=True, show=True, 
            show_labels=True, 
            show_conf=True, 
            conf = 0.25)

        #plt.imshow(res[0].plot())
        #plt.show()



