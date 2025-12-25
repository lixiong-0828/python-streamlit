import streamlit as st
import pandas as pd
import numpy as np


st.title("welcome to Streamlit! 👋" )
st.write("hello world!  This is my first Streamlit app.")
# Create a sample DataFrame
df = pd.DataFrame(np.random.rand(50, 2) / [50, 50] + [38.86, 121.55], columns=['lat', 'lon'])

st.map(df)



