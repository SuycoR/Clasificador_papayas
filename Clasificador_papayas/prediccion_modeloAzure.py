import urllib.request
import json
import numpy as np
from PIL import Image

# Cargar y preprocesar imagen
img = Image.open("content/PAPAYAGIANCARLITO.jpg").resize((224, 224)).convert("RGB")
img_array = np.array(img)  # shape: (224, 224, 3)
img_array = np.expand_dims(img_array, axis=0)  # shape: (1, 224, 224, 3)

# Preparar payload
data = {
    "data": img_array.tolist()
}
body = str.encode(json.dumps(data))

# Endpoint y clave
url = 'https://cp-azuremachinelearning-jiaxl.brazilsouth.inference.ml.azure.com/score'
api_key = '9JhLa1AOFxdUABA8N4jkHeavLVfI1OVSKuq817o2fdOKnKNDaMFFJQQJ99BFAAAAAAAAAAAAINFRAZMLtqbK'

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + api_key
}

# Hacer request
req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    print("Respuesta del modelo:", result.decode())
except urllib.error.HTTPError as error:
    print("FALLÓ:", error.code)
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
