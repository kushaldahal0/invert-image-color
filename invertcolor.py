import os
from PIL import Image, ImageOps
from tkinter import Tk, filedialog
import ctypes

def invert_image_colors(image_path):
    with Image.open(image_path) as img:
        inverted_image = ImageOps.invert(img.convert('RGB'))
        inverted_image.save(image_path.replace('.', '_inverted.'))

def main():
    # Initialize Tkinter root
    root = Tk()
    root.withdraw()  # Hide the main window

    # Open file dialog to select multiple files
    file_paths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )

    # Process each selected file
    for file_path in file_paths:
        if os.path.isfile(file_path):
            try:
                invert_image_colors(file_path)
                print(f"Processed: {file_path}")
            except Exception as e:
                print(f"Failed to process {file_path}: {e}")

if __name__ == "__main__":
    main()
