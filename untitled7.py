import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
from scipy import stats
import pickle
import os  # Import os module for path manipulation

# Define function to load data
@st.experimental_singleton
def load_data():
    file_path = 'new_dfs.pickle'
    if os.path.exists(file_path):
        with open(r"C:\Users\User\Downloads\new_dfs.pickle", 'rb') as handle:
            data = pickle.load(handle)
        return data

# Load data
new_dfs = load_data()

# Check if data loaded successfully
if new_dfs is not None:
    # Streamlit app
    st.title('Spice Price Prediction')

    # Extracting unique spices and states for the dropdown
    spices = list(set([k[0] for k in new_dfs.keys()]))
    selected_spice = st.selectbox('Select Spice', spices)

    # Filter states based on selected spice
    states = [k[1] for k in new_dfs.keys() if k[0] == selected_spice]
    selected_state = st.selectbox('Select State', states)

    # Select number of months for prediction
    num_months = st.number_input('Select number of months for prediction', min_value=1, max_value=12, value=3)

    # Button to trigger prediction
    if st.button('Predict'):
        # Your prediction logic here...
        st.write("Prediction logic will be executed here.")
