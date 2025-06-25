import tensorflow as tf

# 1️⃣ Cargar el modelo previamente entrenado (.h5)
model = tf.keras.models.load_model("modelo_mobilenetv2_papayas.h5")

# 2️⃣ Convertir a TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# 3️⃣ Guardar el modelo convertido
with open("modelo_papayas.tflite", "wb") as f:
    f.write(tflite_model)

print("✅ Modelo exportado a: modelo_papayas.tflite")


