import streamlit as st
import pandas as pd
import numpy as np
import kagglehub  # Import kagglehub to handle the dataset download

# Set page layout
st.set_page_config(layout="wide")

# Download and read the data from Kaggle
@st.cache
def load_data():
    kagglehub.dataset_download('amirmotefaker/supply-chain-dataset', path='supply_chain_data.csv')
    return pd.read_csv("supply_chain_data.csv")

# Load the dataset
df = load_data()

# Create a sidebar menu
menu = ["Home", "SKU Monitoring", "About"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.title("Welcome to SKU Monitoring App")
    st.write("Use the menu to navigate.")
    
elif choice == "SKU Monitoring":
    st.title("SKU Monitoring Dashboard")

    # Split the data based on availability
    availability_less_50 = df[df["Availability"] < 50]
    availability_more_80 = df[df["Availability"] > 80]

    # Animate row movements using st.dataframe
    left_col, right_col = st.columns(2)
    with left_col:
        st.subheader("Availability < 50")
        # Add random noise to simulate changes
        availability_less_50["Availability"] = availability_less_50["Availability"] + np.random.randint(-5, 6, size=len(availability_less_50))
        st.dataframe(availability_less_50)

    with right_col:
        st.subheader("Availability > 80")
        # Add random noise to simulate changes
        availability_more_80["Availability"] = availability_more_80["Availability"] + np.random.randint(-5, 6, size=len(availability_more_80))
        st.dataframe(availability_more_80)
    
elif choice == "About":
    st.title("About this App")
    st.write("This is a simple SKU Monitoring application created with Streamlit using a Kaggle dataset.")
