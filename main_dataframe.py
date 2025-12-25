import streamlit as st
import pandas as pd
import numpy as np

st.title("welcome to Streamlit! 👋")

st.write("hello world!  This is my first Streamlit app.")

# Create a sample DataFrame
df = pd.DataFrame({
    'A': np.random.randn(10),
    'B': np.random.randn(10),
    'C': np.random.randn(10)        
})

st.write("Here is a sample DataFrame:")

# write() displays a static table. but can sortable.
st.write("Here is the DataFrame displayed using st.write():")
st.write(df)

# dataframe() displays an interactive table.
st.write("Here is the same DataFrame displayed as an interactive table:")
st.dataframe(df.style.highlight_max(axis=0),width=700, height=400)

# table() displays a static table.can't scroll and sortable.
st.write("Here is the same DataFrame displayed as a static table:")
st.table(df)