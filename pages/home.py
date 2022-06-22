import streamlit as st

def app():
    #title to home page
    st.title("COVID-19 Detection")

    #Image path
    st.image("./download.jpg")

    #Simple text to project
    
    st.title("Content:")
    st.write("Coronavirus disease 2019 (COVID-19) is a contagious disease caused by a virus, the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The first known case was identified in Wuhan, China, in December 2019. The disease spread worldwide, leading to the COVID-19 pandemic")
    st.title("Computed Tomography (CT):")
    st.write("One of the promising methods for early detection of Coronavirus Disease 2019 (COVID-19) among symptomatic patients is to analyze chest Computed Tomography (CT) scans of individuals using Deep Learning (DL) techniques. Typical visible features on CT scan include bilateral multilobar ground-glass opacities with a peripheral or posterior distribution. COVID-19 can be identified with higher precision using CT scan than RT-PCR.")
    st.title("Project Description:")
    st.write("This project proposes a sequential convolutional neural network to detect COVID-19 from chest CT scans of an individual")