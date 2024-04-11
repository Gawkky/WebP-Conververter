import os

# Function to get the absolute path of the image file
def get_absolute_file_path(image):
    return os.path.abspath(image)

# Example usage:
image_file = "DTP_8253.jpg"
absolute_path = get_absolute_file_path(image_file)
print("Absolute path of the image file:", absolute_path)

# Check if the file exists
if os.path.exists(absolute_path):
    print("Image file exists.")
else:
    print("Image file does not exist or cannot be accessed.")

# Check file permissions
if os.access(absolute_path, os.R_OK):
    print("File is readable.")
else:
    print("File is not readable or permissions are insufficient.")
