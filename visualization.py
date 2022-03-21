import os
from random import shuffle
from tqdm import tqdm
import cv2
import numpy as np
from labelling_image import my_label
def data_for_vizualization():
    Vdata = []
    for img in tqdm(os.listdir("Image for Vizualization")):
        path = os.path.join("Image for Vizualization",img)
        img_num = img.split('.')[0]
        img_data = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        img_data = cv2.resize(img_data,(50,50))
        Vdata.append([np.array(img_data),img_num])
    shuffle(Vdata)
    return Vdata

Vdata = data_for_vizualization()