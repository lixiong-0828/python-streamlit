import streamlit as st
import pandas as pd
import numpy as np

st.title("welcome to Streamlit! 👋")

st.write("hello world!  This is my first Streamlit app.")

# Create a sample DataFrame
df = pd.DataFrame({
    'A': np.random.rand(20),
    'B': np.random.rand(20),
    'C': np.random.rand(20)        
})

# Line chart
st.write("Here is a line chart of the sample DataFrame:")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

