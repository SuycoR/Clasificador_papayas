import os
import json
import logging
import numpy as np
from tensorflow.keras.models import load_model

# Configura logging
logging.basicConfig(level=logging.INFO)

def init():
    global model

    # Ruta del modelo cargado automáticamente por Azure
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "modelo_mobilenetv2_papayas.h5")
    model = load_model(model_path)

    logging.info("Modelo cargado correctamente desde: %s", model_path)

def run(raw_data):
    try:
        logging.info("Solicitud recibida")

        # Parseo del JSON
        data = json.loads(raw_data)

        # Se espera que venga como {"data": [[[...]]]} de tamaño (1, 224, 224, 3)
        img_array = np.array(data["data"])

        # Predicción
        preds = model.predict(img_array)
        class_idx = int(np.argmax(preds))

        logging.info("Predicción completada: Clase %d", class_idx)

        return {
            "predicted_class": class_idx,
            "probabilities": preds.tolist()
        }

    except Exception as e:
        logging.error("Error en la predicción: %s", str(e))
        return {"error": str(e)}
