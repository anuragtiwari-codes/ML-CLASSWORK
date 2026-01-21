import os
from PIL import Image

input_folder = "../Output_PNG"
output_folder = "../Output_EPS"

os.makedirs(output_folder, exist_ok=True)

existing_eps = {os.path.splitext(f)[0] for f in os.listdir(output_folder) if f.lower().endswith(".eps")}

for file in os.listdir(input_folder):
    if file.lower().endswith(".png"):
        base_name = os.path.splitext(file)[0]

        if base_name in existing_eps:
            print(f"Skipping (already converted): {base_name}.eps")
            continue

        png_path = os.path.join(input_folder, file)
        eps_path = os.path.join(output_folder, base_name + ".eps")

        img = Image.open(png_path).convert("RGB")
        img.save(eps_path, "EPS")
        print(f"Converted: {file} -> {base_name}.eps")

print("\nConversion completed! Only new PNGs processed.")
