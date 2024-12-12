import tensorflow as tf
import numpy as np
import cv2
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

model = MobileNetV2(weights='imagenet')

image_path = './Images/Panda.jpg'  
img = image.load_img(image_path, target_size=(224, 224))


img_array = image.img_to_array(img)  
img_array = np.expand_dims(img_array, axis=0)  
img_array = preprocess_input(img_array)  


predictions = model.predict(img_array)


top_predictions = decode_predictions(predictions, top=3)[0]  
print("Top Predictions:")
for i, (imagenet_id, label, score) in enumerate(top_predictions):
    print(f"{i + 1}: {label} ({score:.2f})")
original_image = cv2.imread(image_path)
original_image = cv2.resize(original_image, (800, 800))  

top_label = top_predictions[0][1]
cv2.putText(original_image, f"Prediction: {top_label}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv2.imshow("Object Recognition", original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()