from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)
model = load_model("modelo_mobilenetv2_papayas.h5")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    img_array = np.array(data["data"])  # Espera shape: (1, 224, 224, 3)
    preds = model.predict(img_array)
    class_idx = int(np.argmax(preds))
    return jsonify({
        "predicted_class": class_idx,
        "probabilities": preds.tolist()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
