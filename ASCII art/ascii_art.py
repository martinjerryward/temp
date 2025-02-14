import os
from PIL import Image
import numpy as np

# Define ASCII character set (darkest to lightest)
ASCII_CHARS = "@%#*+=-:. "

def image_to_ascii(image_path, width=100):
    # Open image and convert to grayscale
    image = Image.open(image_path).convert("L")
    
    # Calculate aspect ratio correction
    aspect_ratio = image.height / image.width
    new_height = int(width * aspect_ratio * 0.55)  # 0.55 corrects for character height
    image = image.resize((width, new_height))

    # Convert pixels to ASCII characters
    pixels = np.array(image)
    ascii_image = "\n".join("".join(ASCII_CHARS[pixel // 32] for pixel in row) for row in pixels)

    return ascii_image

# Get the script's directory and construct the relative image path
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "example.jpg")

# Example usage
ascii_art = image_to_ascii(image_path, width=100)
print(ascii_art)
