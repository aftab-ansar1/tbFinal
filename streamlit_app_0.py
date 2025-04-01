import streamlit as st
import pickle
# import tables

import numpy as np
from preprocessing_file import image_preprocessing

st.header('Tuberculosis Detection', divider = 'gray')
st.subheader('_Upload Your X-ray Image to Check the TB Detection_', divider = 'blue')
tab1, tab2 = st.tabs(['Upload Image', 'Camera Input'])
with tab1:
    uploaded_img = st.file_uploader('File Upload', type = ['jpg', 'jpeg'])
    try:
        st.image(uploaded_img)


        img_array = image_preprocessing(uploaded_img)

        with open('tb_predictor_mode.pkl', 'rb') as model_file:
            model = pickle.load(model_file)


        # # Get prediction
        prediction = model.predict(img_array)

        # Print prediction
        print("Prediction:", prediction)

        #binary classification
        label = "Positive" if prediction[0][0] > 0.5 else "Negative"
        if label == "Positive":
            st.subheader(f"Tuberclousis Detection :red[{label}]")
        else:
            st.subheader(f"Tuberclousis Detection :green[{label}]")
    except:
        print('No File Uploaded')
        
with tab2:
    enable = st.checkbox("Enable camera")
    uploaded_img = st.camera_input("Take a picture", disabled=not enable)
    
    # uploaded_img = st.camera_input('click image',)
    try:
        st.image(uploaded_img)


        img_array = image_preprocessing(uploaded_img)

        with open('tb_predictor_mode.pkl', 'rb') as model_file:
            model = pickle.load(model_file)


        # # Get prediction
        prediction = model.predict(img_array)

        # Print prediction
        print("Prediction:", prediction)

        #binary classification
        label = "Positive" if prediction[0][0] > 0.5 else "Negative"
        if label == "Positive":
            st.subheader(f"Tuberclousis Detection :red[{label}]")
        else:
            st.subheader(f"Tuberclousis Detection :green[{label}]")
    except:
        print('No File Uploaded')