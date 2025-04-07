from PIL import Image
import numpy as np

def preprocess_image(image: Image.Image):
    image = image.convert("L")  # Escala de grises
    image = image.resize((28, 28))  # Tamaño MNIST
    image_array = np.array(image).astype("float32") / 255.0
    return image_array
