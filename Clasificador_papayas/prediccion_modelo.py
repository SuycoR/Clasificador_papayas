
import requests
import numpy as np
from tensorflow.keras.preprocessing import image

img_path = "resized/test/unmature/unmature_003.jpg"
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img) 
img_array = np.expand_dims(img_array, axis=0)

response = requests.post(
    "http://localhost:5000/predict",
    json={"data": img_array.tolist()}
)

print(response.json())