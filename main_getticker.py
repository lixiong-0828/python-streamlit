import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf


st.title('Stock Ticker Data Viewer')
aapl = yf.ticker("IBM")
data = aapl.history(period="1d")
st.write(data)