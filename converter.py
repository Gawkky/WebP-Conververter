import os
import subprocess
import shutil
from os.path import splitext

# Define the directory names and extensions
dir_name = 'webp'
extensions = ('.png', '.jpg', '.jpeg')
webp_location = os.path.join(os.curdir, dir_name)
photos_location = os.path.join(os.curdir, 'photos')

# Define the conversion function
def convert_to_webp(image, output_file):
    try:
        quality = 80
        cwebp_path = r"C:\Users\theeuwje\AppData\Local\WebP\bin\cwebp.exe"
        command = f'"{cwebp_path}" -q {quality} "{image}" -o "{output_file}"'
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        # Check if there was any error during the conversion
        if error:
            print(f"Conversion failed for {image}: {error.decode()}")
        else:
            print(f"Conversion successful for {image}")

    except Exception as e:
        print(f"An error occurred during conversion: {e}")

# Define the function to process directories
def process_directory(current_path, webp_path):
    for root, dirs, files in os.walk(current_path):
        for file in files:
            if file.lower().endswith(extensions):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, current_path)
                output_dir = os.path.join(webp_path, relative_path)
                os.makedirs(output_dir, exist_ok=True)
                output_file = os.path.join(output_dir, splitext(file)[0] + '.webp')
                convert_to_webp(file_path, output_file)

# Create the 'webp' directory if it doesn't exist
if not os.path.exists(webp_location):
    os.mkdir(webp_location)

# Process the 'photos' directory
process_directory(photos_location, webp_location)

shutil.make_archive(webp_location, 'zip', webp_location)