from tensorflow.keras.models import load_model as keras_load_model
import numpy as np

def load_model():
    return keras_load_model("model/mnist_final_model.keras")

def predict_digit(model, image_array):
    image_array = image_array.reshape(1, 28, 28, 1)  # Formato MNIST
    prediction = model.predict(image_array)
    return int(np.argmax(prediction))
