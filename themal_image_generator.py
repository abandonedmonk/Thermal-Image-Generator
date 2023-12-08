import os
import numpy as np
from PIL import Image

def generate_thermal_image(size=(256, 256), temperature_range=(20, 100)):
    image = np.random.uniform(temperature_range[0], temperature_range[1], size)
    return image

def save_image(image, directory, filename):
    if not os.path.exists(directory):
        os.makedirs(directory)
    path = os.path.join(directory, filename)
    im = Image.fromarray(image.astype(np.uint8))
    im.save(path)

if __name__ == "__main__":
    output_directory = "Images"
    num_images = 1

    for i in range(num_images):
        thermal_image = generate_thermal_image()
        save_image(thermal_image, output_directory, f"thermal_image_{i}.png")
