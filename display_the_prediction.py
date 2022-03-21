import matplotlib.pyplot as plt   # pip install matplotlib
from visualization import Vdata
import numpy as np
## Creating the model
import warnings
warnings.filterwarnings('ignore')
import tensorflow as tf
from model_creation import model
fig = plt.figure(figsize=(20,20))
for num, data in enumerate(Vdata[:20]):
    img_data = data[0]
    y = fig.add_subplot(5,5, num+1)
    image = img_data
    data = img_data.reshape(50,50,1)
    model_out = model.predict([data])[0]
    
    if np.argmax(model_out) == 0:
        my_label = 'Deepan'
    elif np.argmax(model_out) == 1:
        my_label = 'Ritik'
    
        
    y.imshow(image, cmap='gray')
    plt.title(my_label)
    
    y.axes.get_xaxis().set_visible(False)
    y.axes.get_yaxis().set_visible(False)
plt.show()