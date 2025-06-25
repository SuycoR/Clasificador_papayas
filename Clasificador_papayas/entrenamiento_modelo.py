import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.callbacks import EarlyStopping


# 📁 Rutas y configuración
train_dir = "resized/train"
val_dir   = "resized/valid"
test_dir  = "resized/test"

img_size = (224, 224)
batch_size = 32
epochs = 30

# 📦 Cargar datasets directamente desde sus carpetas
train_ds = image_dataset_from_directory(
    train_dir,
    image_size=img_size,
    batch_size=batch_size
)

val_ds = image_dataset_from_directory(
    val_dir,
    image_size=img_size,
    batch_size=batch_size
)

test_ds = image_dataset_from_directory(
    test_dir,
    image_size=img_size,
    batch_size=batch_size
)

# 🏷️ Guardar nombres de clases
class_names = train_ds.class_names

# ⚙️ Prefetch para eficiencia
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
val_ds   = val_ds.prefetch(buffer_size=AUTOTUNE)
test_ds  = test_ds.prefetch(buffer_size=AUTOTUNE)

# 🔧 Construir modelo con MobileNetV2
base_model = MobileNetV2(
    input_shape=img_size + (3,),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False  # Congelar

model = models.Sequential([
    layers.Rescaling(1./255, input_shape=img_size + (3,)),
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.2),
    layers.Dense(len(class_names), activation='softmax')
])

# 🧪 Compilar
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 🛑 EarlyStopping
early_stop = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True
)

# 🚀 Entrenar
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs,
    callbacks=[early_stop]
)

# 💾 Guardar modelo
model.save("modelo_mobilenetv2_papayas.h5")

# 🎯 Evaluar en test
test_loss, test_acc = model.evaluate(test_ds)
print(f"🎯 Precisión final en test: {test_acc:.2%}")
