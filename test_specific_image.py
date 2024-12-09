import cv2
import numpy as np
from tensorflow import keras

# Load the trained model
model = keras.models.load_model("fine_tuned_vgg16_model.keras")

# Load the image
image_path = "m340i.jpg"  # Replace with the actual path
img = cv2.imread(image_path)
img = cv2.resize(img, (224, 224))
img = img / 255.0
img = np.expand_dims(img, axis=0)

# Get the predicted class probabilities
predictions = model.predict(img)

# Get the predicted class index
predicted_class_index = np.argmax(predictions, axis=1)[0]

# Get the manufacturer's class (replace with the actual class index)
manufacturers_class = 4  # Example class index

# Print the results
if predicted_class_index == manufacturers_class:
    print("Correctly predicted!")
else:
    print("Incorrect prediction.")
    print("Predicted class index:", predicted_class_index)
    print("Manufacturer's class:", manufacturers_class)