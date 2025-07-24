import streamlit as st
import numpy as np
import pickle

# Load the saved model and scaler
model = pickle.load(open("regmodel.pkl", "rb"))
scaler = pickle.load(open("scaling.pkl", "rb"))

# Streamlit App
def main():
    st.title("House Price Prediction App")
    st.subheader("Enter the house features to predict its price")

    # Input fields
    MedInc = st.number_input("Median Income", min_value=0.00, format="%.2f")
    HouseAge = st.number_input("House Age (years)", min_value=0, value=0, step=1)
    AveRooms = st.number_input("Average Number of Rooms", min_value=0, value=0, step=1)
    AveBedrms = st.number_input("Average Number of Bedrooms", min_value=0, value=0, step=1)
    Population = st.number_input("Block Group Population", min_value=1, value=1, step=1)
    AveOccup = st.number_input("Average Household Occupants", min_value=1, value=1, step=1)
    Latitude = st.number_input("Latitude", min_value=32.0, max_value=42.0, format="%.4f")
    Longitude = st.number_input("Longitude", min_value=-125.0, max_value=-113.0, format="%.4f")

    if st.button("Predict Price"):
        # Prepare the input
        input_data = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population,
                                AveOccup, Latitude, Longitude]])
        scaled_input = scaler.transform(input_data)
        prediction = model.predict(scaled_input)
        st.success(f"Estimated House Price: **${prediction[0]*100_000:,.2f}**")

   

if __name__ == '__main__':
    main()
