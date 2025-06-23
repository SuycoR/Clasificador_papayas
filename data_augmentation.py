import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array

# Configuración
base_dir = "resized/train"
augmentations_per_image = 5

datagen = ImageDataGenerator(
    rotation_range=25,
    width_shift_range=0.15,
    height_shift_range=0.15,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

for class_name in os.listdir(base_dir):
    class_path = os.path.join(base_dir, class_name)
    if not os.path.isdir(class_path):
        continue

    print(f"\n🔄 Clase: {class_name}")
    count = 0

    for img_name in os.listdir(class_path):
        if img_name.startswith("aug_"):
            continue  # evitar aumentar aumentadas

        img_path = os.path.join(class_path, img_name)
        try:
            img = load_img(img_path)
            x = img_to_array(img)
            x = x.reshape((1,) + x.shape)

            prefix = f"aug_{os.path.splitext(img_name)[0]}"
            i = 0
            for batch in datagen.flow(
                x,
                batch_size=1,
                save_to_dir=class_path,
                save_prefix=prefix,
                save_format='jpg'
            ):
                i += 1
                count += 1
                if i >= augmentations_per_image:
                    break

        except Exception as e:
            print(f"⚠️ Error en {img_name}: {e}")

    print(f"✅ Aumentadas generadas: {count}")

print("\n✅ Proceso completado.")