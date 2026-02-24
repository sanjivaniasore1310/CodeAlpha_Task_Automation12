import os
import shutil

# ====== SETTINGS ======
source_folder = "source_images"
destination_folder = "moved_images"
image_extensions = (".jpg", ".jpeg", ".png", ".webp")

# ====== CREATE FOLDERS IF NOT EXIST ======
if not os.path.exists(source_folder):
    os.makedirs(source_folder)
    print("Created 'source_images' folder.")
    print("Please add image files and run the script again.")
    exit()

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# ====== MOVE FILES ======
count = 0

for file in os.listdir(source_folder):
    if file.lower().endswith(image_extensions):
        src_path = os.path.join(source_folder, file)
        dest_path = os.path.join(destination_folder, file)

        # Prevent overwriting files
        base, extension = os.path.splitext(file)
        new_dest_path = dest_path
        i = 1
        while os.path.exists(new_dest_path):
            new_dest_path = os.path.join(destination_folder, f"{base}_{i}{extension}")
            i += 1

        shutil.move(src_path, new_dest_path)
        count += 1

# ====== RESULT ======
if count > 0:
    print(f"{count} image(s) moved successfully!")
else:
    print("No image files found in source_images folder.")