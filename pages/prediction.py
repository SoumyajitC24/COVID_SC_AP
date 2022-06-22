"""This is the prediction page of the web app"""

# Import necessary modules
import streamlit as st
import numpy as np

import tensorflow as tf
from tensorflow.keras import preprocessing
import cv2
from cv2 import cvtColor, COLOR_BGR2GRAY
from PIL import Image,ImageOps

from model import load_model

def app():
    """This function runs the prediction page"""

    # Create label values for the prediction
    #label = ['glioma_tumor' , 'meningioma_tumor' , 'no_tumor' , 'pituitary_tumor']
    label = ['CT_COVID', 'CT_NonCOVID']

    # Take image input
    image = st.file_uploader("Upload the Chest CT scan", type=['png','jpeg', 'jpg'])

    # If image then show the image and preprocess it.
    if image:
        st.image(image , width = 325)

        images = Image.open(image)
        images = ImageOps.grayscale(images)
        images = images.resize((256,256))
        images = np.array(images)
        #img = cv2.cvtColor(images, COLOR_BGR2GRAY)
        img = preprocessing.image.img_to_array(images)
        img = np.expand_dims(img, axis=0)

    # Create a button to get the prediction values on click
    if (st.button("Predict")):
        # load the model
        model = load_model()

        # predict value
        pred_value = ""
        prediction = model.predict(img)
        pred_value = label[np.argmax(prediction)]

        # Show prediction values
        confidence = np.amax(prediction) * 100
        #Print prediction
        if(confidence > 70): 
            if(pred_value == 'CT_COVID'):
                st.success("COVID detected!! Take precautionary steps immediately.")
            else:
                st.success("No COVID detected.")
            st.info(f"Confidence:{confidence}%")    
        else:
            print(type(confidence))
            st.warning("Cannot be determined. Please try again!")