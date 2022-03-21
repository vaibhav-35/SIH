import numpy as np
def my_label(image_name):
    name = image_name.split('.')[-3]
    
    if name == "Deepan":
        return np.array([1,0])
    elif name == "Ritik":
        return np.array([0,1])
    