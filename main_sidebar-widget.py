import streamlit as st
import pandas as pd
import numpy as np
import PIL.Image as Image


st.title("welcome to Streamlit! 👋" )
st.sidebar.write("sidebar widget example")

option = st.sidebar.selectbox("Choose an number", list(range(1, 11)))
'your selected number is : ', option

text = st.sidebar.text_input("Enter your intresting thing" )
'your interesting is : ', text

condition = st.sidebar.slider("How much do you like Streamlit?", 0, 100, 50)
'You like Streamlit ', condition, '%'

# two columns layout
st.write("----------------------------------------------------")
st.write("Two columns layout example")
col1, col2 = st.columns(2)
button1 = col1.button("Button in column 1")
button2 = col2.button("Button in column 2")
with col1:
    st.header("Column 1")
    st.write("This is column 1")
with col2:
    st.header("Column 2")
    st.write("This is column 2")

if button1:
    st.write("You clicked the button in column 1")
if button2:
    st.write("You clicked the button in column 2")
    
# expander layout
st.write("----------------------------------------------------")
st.write("Expander layout example")
expander = st.expander("Click to expand/collapse")
with expander:
    st.write("This is inside the expander")
    if st.button("Button inside expander"):
        st.write("You clicked the button inside the expander")
        img = Image.open("my_pic.jpg")
        st.image(img, caption='Streamlit Logo', use_column_width=True)
    if st.button("close image"):
        st.write("Image closed")
        img = None
    if st.button("Close expander"):
        expander.empty()    
        
st.write("This is outside the expander")



