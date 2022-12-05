import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image

# st.set_page_config(layout="wide")
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 1.1rem;
                    padding-bottom: 1rem;
                    padding-left: 1rem;
                    padding-right: 0rem;
                }
                
                
                div.appview-container.css-1wrcr25.egzxvld4{
                font-family: Arial;
                width: 85%;
                margin-left: 0%;
                margin-right: 0%;
                }
        </style>
        """, unsafe_allow_html=True)

main, info = st.columns([1,1])

with main:
    st.markdown('### Pet Information')
    
    species = st.radio("Select your pet's species", ('Cat', 'Dog'), horizontal = True)
    
    if species=='Cat':
#         gender = st.radio(
#         "Gender", ('Male', 'Female'), horizontal = True)
#         if gender=='Male' or gender=='Female':
        lifestage = st.radio("Select your pet's lifestage", ('Adult', 'Growing'), horizontal = True)
        if lifestage == 'Adult':
            condition = st.radio("Select condition", ('Intact', 'Neutered', 'Obese Prone'), horizontal = True)
            activity = st.radio("Select activity level",('Low', 'Normal', 'High'), horizontal = True)
                
    
    if species=='Dog':
#         gender = st.radio(
#         "Gender", ('Male', 'Female'), horizontal = True)
#         if gender=='Male' or gender=='Female':
        lifestage = st.radio("Select your pet's lifestage", ('Adult', 'Growing'), horizontal = True)
        if lifestage == 'Adult':
            condition = st.radio(
                "Condition", ('Intact', 'Neutered', 'Obese Prone'), horizontal = True)
            activity = st.radio("Activity Level",('Low', 'Normal', 'High'), horizontal = True)
        elif lifestage=='Growing':
            condition = st.radio("Select condition", ('Less than 4 months', 'More than 4 months'), horizontal = True)
            activity = st.radio("Select activity level",('Low', 'Normal', 'High'), horizontal = True)
                    
# st.markdown("# Enter your pet's weigth in kg")    
col1, col2, col3=st.columns([0.7, 1, 2])



with col1:

    weight = st.number_input(label = 'Weight',
                            step=1.0)
rer = 70 * (weight ** 0.75)
bw = weight ** 0.75
if lifestage == 'Adult':
    if condition == 'Intact' and species == 'Cat':
        kcal_per_day = 1.4 * rer
        protien_per_day = 3.97 * bw
        fat_per_day = 2.2 * bw
    elif condition == 'Neutered' and species == 'Cat':
        kcal_per_day = 1.2 * rer
        protien_per_day = 3.97 * bw
        fat_per_day = 2.2 * bw
    elif condition == 'Obese Prone' and species == 'Cat':
        kcal_per_day = rer
        protien_per_day = 3.97 * bw
        fat_per_day = 2.2 * bw
    elif condition == 'Intact' and species == 'Dog':
        kcal_per_day = 1.8 * rer
        protien_per_day = 2.62 * bw
        fat_per_day = 1.3 * bw
    elif condition == 'Neutered' and species == 'Dog':
        kcal_per_day = 1.6 * rer
        protien_per_day = 2.62 * bw
        fat_per_day = 1.3 * bw
    elif condition == 'Obese Prone' and species == 'Dog':
        kcal_per_day = 1.4 * rer
        protien_per_day = 2.62 * bw
        fat_per_day = 1.3 * bw
elif lifestage == 'Growing':
    if species == 'Cat':
        kcal_per_day = 2.5 * rer
        protien_per_day = 9.4 * bw
        fat_per_day = 4.7 * bw
    elif species == 'Dog':
        if condition == 'Less than 4 months':
            kcal_per_day = 3 * rer
            protien_per_day = 9.7 * bw
            fat_per_day = 5.9 * bw
        elif condition == 'More than 4 months':
            kcal_per_day = 2 * rer
            protien_per_day = 12.75 * bw
            fat_per_day = 5.9 * bw

with info:
    if species=='Dog':
        img = Image.open("D:\\Streamlit\\streamlit\\Scripts\\dog_image.png")
        st.image(img,
                width=280)
#         fig = px.imshow(img,
#                        width=[10, 50])
#         st.plotly_chart(fig)
    elif species=='Cat':
        img = Image.open("D:\\Streamlit\\streamlit\\Scripts\\cat_image.png")
        st.image(img,
                width=280)
#         fig = px.imshow(img,
#                        width=[10, 50])
#         st.plotly_chart(fig)
    st.markdown("### Requirements")
    # # st.markdown('##### Calories required per day:')
    # st.write('Calories required per day:' ,str(round(kcal_per_day,0)), 'kcal')
    # # st.markdown('##### Protien required per day:', protien_per_day)
    # st.write('Protien required per day:', str(round(protien_per_day,0)), 'g')
    # # st.markdown('##### Fat required per day:', fat_per_day)
    # st.write('Fat required per day:', str(round(fat_per_day,0)), 'g')
    
#     st.markdown(a + b + c,
#                unsafe_allow_html=True)
    st.markdown(f'<p style="display:inline;" > Energy (kcal/day):</p> <p style="color:#fe9a0a;display:inline;">{str(round(kcal_per_day,0))}</p>',
               unsafe_allow_html=True)
    st.markdown(f'<p style="display:inline;" > Fat (g/day):</p> <p style="color:#fe9a0a;display:inline;">{str(round(fat_per_day,0))}</p>',
               unsafe_allow_html=True)
    st.markdown(f'<p style="display:inline;" > Protein (g/day):</p> <p style="color:#fe9a0a;display:inline;">{str(round(protien_per_day,0))}</p>',
               unsafe_allow_html=True)