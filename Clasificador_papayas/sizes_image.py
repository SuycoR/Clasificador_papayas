import os
from PIL import Image

# Ruta base del dataset
base_dir = "papaya_image/train"
output_file = "image_sizes.txt"

# Lista para guardar los resultados
result_lines = []

# Recorrer las carpetas por clase
for class_name in os.listdir(base_dir):
    class_path = os.path.join(base_dir, class_name)

    if not os.path.isdir(class_path):
        continue

    result_lines.append(f"\nClase: {class_name}")

    for img_name in os.listdir(class_path):
        img_path = os.path.join(class_path, img_name)

        try:
            with Image.open(img_path) as img:
                width, height = img.size
                result_lines.append(f"{img_name}: {width}x{height}")
        except Exception as e:
            result_lines.append(f"{img_name}: ERROR ({e})")

# Guardar los resultados en el archivo de texto
with open(output_file, "w") as f:
    f.write("\n".join(result_lines))

print(f"✅ Archivo guardado como: {output_file}")
