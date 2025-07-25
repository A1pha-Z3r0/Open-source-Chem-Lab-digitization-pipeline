
import cv2
import numpy as np


class ImagePreprocess():
    def __init__(self,):
        pass
    def normalize(self,image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Normalize grayscale image
        normalized_gray_image = cv2.normalize(
            gray_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

        # Convert normalized grayscale image back to color

        return cv2.cvtColor(
            normalized_gray_image, cv2.COLOR_GRAY2BGR)
        
    def noise_removal(self,image):
        return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15)
        
    def thresholding(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        return cv2.cvtColor(
            image, cv2.COLOR_GRAY2BGR)



    
        

    