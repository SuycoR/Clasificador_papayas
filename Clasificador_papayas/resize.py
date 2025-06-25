import os
from PIL import Image, ImageOps

# Configuración
input_base_dir = "papaya_image/train"
output_base_dir = "resized/train"
target_size = (224, 224)
background_color = (255, 255, 255)  # Blanco

# Procesar imágenes
for class_name in os.listdir(input_base_dir):
    input_class_path = os.path.join(input_base_dir, class_name)
    output_class_path = os.path.join(output_base_dir, class_name)

    if not os.path.isdir(input_class_path):
        continue

    os.makedirs(output_class_path, exist_ok=True)

    for img_name in os.listdir(input_class_path):
        input_img_path = os.path.join(input_class_path, img_name)
        output_img_path = os.path.join(output_class_path, img_name)

        try:
            with Image.open(input_img_path) as img:
                # Convertir a RGB si es necesario
                img = img.convert("RGB")
                # Redimensionar manteniendo proporción y rellenar con blanco
                img.thumbnail(target_size, Image.Resampling.LANCZOS)
                delta_w = target_size[0] - img.size[0]
                delta_h = target_size[1] - img.size[1]
                padding = (delta_w // 2, delta_h // 2, delta_w - (delta_w // 2), delta_h - (delta_h // 2))
                new_img = ImageOps.expand(img, padding, fill=background_color)
                new_img.save(output_img_path)
        except Exception as e:
            print(f"Error con imagen {img_name}: {e}")

import os
resized_classes = os.listdir(output_base_dir)
resized_summary = {cls: len(os.listdir(os.path.join(output_base_dir, cls))) for cls in resized_classes}
import pandas as pd

df_summary = pd.DataFrame.from_dict(resized_summary, orient='index', columns=["Total Imágenes"])
print(df_summary)
df_summary.to_csv("resumen_redimension.txt")