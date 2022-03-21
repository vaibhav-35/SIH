import os
from random import shuffle
from tqdm import tqdm
import cv2
import numpy as np
from labelling_image import my_label
def my_data():
    data = []
    for img in tqdm(os.listdir("data")):
        path = os.path.join("data",img)
        img_data = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        img_data = cv2.resize(img_data,(50,50))
        data.append([np.array(img_data),my_label(img)])
    shuffle(data)
    return data


data = my_data()