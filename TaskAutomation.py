import os
import shutil
from datetime import datetime

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder path does not exist.")
        return

    file_count = 0
    log = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            # Get extension
            ext = filename.split('.')[-1].lower()
            ext_folder = os.path.join(folder_path, ext.upper() + "_Files")

            # Make folder if not exists
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)

            # Move file
            new_location = os.path.join(ext_folder, filename)
            shutil.move(file_path, new_location)

            log.append(f"Moved: {filename} -> {ext_folder}")
            file_count += 1

    # Write log file
    log_file = os.path.join(folder_path, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    with open(log_file, 'w') as f:
        for entry in log:
            f.write(entry + '\n')

    print(f"\n✅ Organized {file_count} files.")
    print(f"📄 Log saved at: {log_file}")

# --------------------------
# 🟢 Run this below section
# --------------------------

# Enter the folder path here
folder_to_organize = input("Enter the full path of the folder to organize: ")
organize_files(folder_to_organize)
