import os
import shutil
from PIL import Image
corrupted_file_detector


# Define the paths
base_dir = 'c:\PetImages'
train_dir = os.path.join(base_dir, 'Train')
validate_dir = os.path.join(base_dir, 'Validate')
corrupted_dir = os.path.join(base_dir, 'Corrupted')

# Create the corrupted directory if it doesn't exist
if not os.path.exists(corrupted_dir):
    os.makedirs(corrupted_dir)

# Function to check and move corrupted files
def check_and_move_corrupted_images(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Try to open the image file
                with Image.open(file_path) as img:
                    img.verify()  # Verify that it is an image
            except (IOError, SyntaxError) as e:
                print(f"Corrupted file found: {file_path}")
                # Move the corrupted file to the corrupted directory
                shutil.move(file_path, os.path.join(corrupted_dir, file))

# Check both Train and Validate directories
check_and_move_corrupted_images(train_dir)
check_and_move_corrupted_images(validate_dir)

print("Corrupted files have been moved to the 'corrupted' folder.")