from flask import Flask, jsonify, send_from_directory, Response
from flask_cors import CORS
import subprocess
import urllib.request
import json
import numpy as np
from PIL import Image
import datetime
from gpiozero import LED, Button
from time import sleep
import os
import cv2

# Variable global para almacenar el último resultado
resultado_json = None

# ------------------ Configuración GPIO ------------------

# GPIO 17 - pin 11 -> Señal LOW si es papaya madura
madura = LED(10)
madura.on()

# GPIO 22 - pin 15 -> Señal del sensor al detectar color
input_color = Button(22, pull_up=False)

# GPIO 10 - pin 19 -> Señal para papaya parcialmente madura
par_madura = LED(17)
par_madura.on()

# GPIO 3 - pin 5 -> Señal que indica fin de predicción
output_prediccion = LED(3)
output_prediccion.on()

# ------------------ Flask App ------------------

app = Flask(__name__)
CORS(app)

# Reemplazo de fswebcam por OpenCV

def capturar_foto(filename="static/imagenPapaya01.jpg"):
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        cv2.imwrite(filename, frame)
    cam.release()

@app.route("/api/tomar_foto", methods=["GET"])
def tomar_foto():
    global resultado_json

    # --- Tomar foto con fswebcam ---
    filename = "static/imagenPapaya01.jpg"
    subprocess.run(["fswebcam", "-r", "640x480", "--no-banner", "-S", "100", filename])
    #capturar_foto(filename)

    # --- Preprocesar imagen ---
    img = Image.open(filename).resize((224, 224)).convert("RGB")
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)

    data = {"data": img_array.tolist()}
    body = str.encode(json.dumps(data))

    # Azure endpoint
    url = '*****'  # Reemplaza con tu endpoint real
    api_key = '****'  # Reemplaza con tu API Key
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        clase = result.get("predicted_class", -1)
        probs = result.get("probabilities", [])

        # --- Control GPIO según la clase ---
        if clase == 0:
            output_prediccion.off()
            sleep(1)

            madura.off()
            sleep(1)
            madura.on()
            output_prediccion.on()
        elif clase == 1:
            output_prediccion.off()
            sleep(1)

            par_madura.off()
            sleep(1)
            par_madura.on()
            output_prediccion.on()
        else:
            # No hacer nada especial
            pass

        resultado_json = {
            "status": "ok",
            "clase": clase,
            "probs": probs,
            "foto_url": "/static/imagenPapaya01.jpg",
            "timestamp": datetime.datetime.now().isoformat()
        }

        return jsonify(resultado_json)

    except urllib.error.HTTPError as error:
        return jsonify({
                "status": "error",
            "code": error.code,
            "info": error.read().decode("utf8", 'ignore')
        })

# --- Cuando se suelta el botón del sensor, toma la foto automáticamente ---
input_color.when_released = tomar_foto

# --- Endpoint para obtener el último resultado sin tomar nueva foto ---
@app.route("/api/resultado", methods=["GET"])
def obtener_resultado():
    global resultado_json
    if resultado_json is None:
        return jsonify({"status": "no_data", "message": "No se ha tomado ninguna foto"})
    return jsonify(resultado_json)

# --- Stream en vivo de la cámara ---
def gen_frames():
    cam = cv2.VideoCapture(0)
    while True:
        success, frame = cam.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/api/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# --- Servir la última foto tomada ---
@app.route('/api/conseguirfoto')
def ultima_foto():
    return send_from_directory(directory="/home/pi/Documents/papayas-proyecto/static", filename="imagenPapaya01.jpg")

# --- Endpoint para tomar una foto de prueba ---
@app.route('/api/foto_prueba')
def foto_prueba():
    filename = "static/imagenPapayas02.jpg"
    subprocess.run(["fswebcam", "-r", "640x480", "--no-banner", "-S", "100", filename])

    return jsonify({"status": "ok", "foto": filename})

# --- Ejecutar la app ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)










