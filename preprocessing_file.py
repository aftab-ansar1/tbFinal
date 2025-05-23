from tensorflow.keras.utils import load_img, img_to_array
import numpy as np

def image_preprocessing(image):
    img = image
    img = load_img(image, target_size=(128, 128))  # Resize to match model input size


    # Convert the image to a NumPy array
    img_array = img_to_array(img)

    # Normalize pixel values (same as during training)
    img_array = img_array / 255.0

    # Add a batch dimension (model expects input shape: [batch_size, height, width, channels])
    return np.expand_dims(img_array, axis=0)



