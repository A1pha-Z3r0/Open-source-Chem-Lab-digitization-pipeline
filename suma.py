import cv2
import numpy as np
import torch 

from doctr.models import ocr_predictor
from doctr.io import read_pdf
from doctr.io import read_img_as_numpy



img_path = "/Users/jona_allwin/developer/projects/portfolio/data_pipeline/test/test_eq.png"

list1 = []

image = cv2.imread(img_path)

from ultralytics import YOLO
from huggingface_hub import hf_hub_download
from matplotlib import pyplot as plt

# Load the weights from our repository
model_path = hf_hub_download(local_dir=".",
                             repo_id="armvectores/yolov8n_handwritten_text_detection",
                             filename="best.pt")
model = YOLO(model_path)

# Do the predictions
res = model.predict(source=img_path, project='.',name='detected', exist_ok=True, save=True, show=False, show_labels=False, show_conf=False, conf=0.5, )

plt.figure(figsize=(15,10))
plt.imshow(res[0].plot())
plt.show()

quit











print(type(image))
print(image.shape)
quit()



image = read_img_as_numpy(img_path)
pages = read_pdf("/Users/jona_allwin/developer/projects/portfolio/data_pipeline/test/three_page.pdf")

print(type(pages))
print(type(image))

list1.append(image)

print(list1[0].shape)

batch = np.stack(list1, axis = 0)
print(batch.shape)

print(batch[0].shape)
print(batch[0].dtype)

for i in batch:
    print(i.shape)


#image1 =  np.ones((3300, 2560,3), dtype=np.uint8)*255

#image2 =  torch.ones((3,3300, 2560), dtype=torch.float32)

model = ocr_predictor('linknet_resnet50', 'master', pretrained= True,)


for i in [0,1,3,4,]:
    print(i)



output = model([batch[0]])
output1 = model(pages)
#output2 = model([image2])
print(output.render())
print(output1.render())
#print(output2.render())

