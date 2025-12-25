import streamlit as st
import pandas as pd
import numpy as np
import PIL.Image as Image


st.title("welcome to Streamlit! 👋" )
st.write("interactive widget example")

option = st.selectbox("Choose an number", list(range(1, 11)))
'your selected number is : ', option

text = st.text_input("Enter your intresting thing" )
'your interesting is : ', text

condition = st.slider("How much do you like Streamlit?", 0, 100, 50)
'You like Streamlit ', condition, '%'


