import os
import re
import shutil
import random
from collections import defaultdict

# Configuración
base_dir = "resized/train"
output_base = "resized"
split_ratio = {"train": 0.7, "valid": 0.2, "test": 0.1}
log_lines = []

# Función mejorada para extraer nombre base
def get_base_name(filename):
    if filename.startswith("aug_"):
        match = re.match(r"aug_([A-Za-z0-9]+_\d+)_\d+_", filename)
        if match:
            return match.group(1)
    else:
        return os.path.splitext(filename)[0]
    return None

# Recorrer todas las clases
for class_name in os.listdir(base_dir):
    class_path = os.path.join(base_dir, class_name)
    if not os.path.isdir(class_path):
        continue

    # Agrupar por nombre base
    grouped = defaultdict(list)
    for fname in os.listdir(class_path):
        base_name = get_base_name(fname)
        if base_name:
            grouped[base_name].append(fname)

    # Mezclar bloques
    all_keys = list(grouped.keys())
    random.shuffle(all_keys)

    # Calcular división
    total = len(all_keys)
    n_train = int(total * split_ratio["train"])
    n_valid = int(total * split_ratio["valid"])
    n_test = total - n_train - n_valid

    splits = {
        "train": all_keys[:n_train],
        "valid": all_keys[n_train:n_train + n_valid],
        "test": all_keys[n_train + n_valid:]
    }

    # Mover archivos
    for split_name, keys in splits.items():
        for key in keys:
            for fname in grouped[key]:
                src_path = os.path.join(class_path, fname)
                dst_dir = os.path.join(output_base, split_name, class_name)
                os.makedirs(dst_dir, exist_ok=True)
                dst_path = os.path.join(dst_dir, fname)
                shutil.move(src_path, dst_path)
            log_lines.append(f"{class_name}/{key} -> {split_name}")

# Guardar log
with open("split_log_fixed.txt", "w") as f:
    for line in log_lines:
        f.write(line + "\n")

print("✅ Split completado. Revisa 'split_log_fixed.txt'")
