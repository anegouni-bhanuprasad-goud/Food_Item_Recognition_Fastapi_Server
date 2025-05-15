from tensorflow.keras.models import load_model # type: ignore
from PIL import Image
import numpy as np

model = load_model("food_model_83%.h5")

async def predict(filepath : str):
   img =  Image.open(filepath).convert("RGB").resize([256,256])
   img_array = np.array(img)
   img_array = np.array(img_array / 255, dtype="float32")
   img_array = np.expand_dims(img_array, axis=0)

   res =  model.predict(img_array)
   predicted_class = np.argmax(res, axis=1)

   items = ['Biryani', 'Butter Naan', 'Chai', 'Chole Bhature', 'Dhokla', 'Gulab Jamun', 'Jalebi', 'Momos', 'Paneer Sabzi', 'Pav Bhaji', 'Rasgulla', 'Samosa']
   class_name = items[predicted_class[0]]

   print("Predicted Class: ", predicted_class[0], " ==> ", class_name)

   return class_name


"""
import os 

while True:
   path = input("Enter the filepath : ")
   if os.path.exists(path):
      pred = predict(path)
      print(f"Model predicted : {pred}")
   else:
       print("File not found")

"""