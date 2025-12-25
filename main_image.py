import streamlit as st
import pandas as pd
import numpy as np
import PIL.Image as Image


st.title("welcome to Streamlit! 👋" )
st.write("image map example")

if st.checkbox("Show Image"):
    # Load an image
    img = Image.open("my_pic.jpg")
    st.image(img, caption='My pic', use_column_width=True)


