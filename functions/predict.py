import json
import pickle
import numpy as np
from flask import Flask, jsonify, request

# Load model and scaler
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

# Initialize Flask app for handling requests
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Extract form values from POST request and convert them to float
    data = [float(x) for x in request.form.values()]
    # Normalize the data using the loaded scaler
    final_input = scalar.transform(np.array(data).reshape(1, -1))
    # Predict output using the loaded regression model
    output = regmodel.predict(final_input)[0]
    # Return prediction result as a JSON response
    return jsonify({"prediction": "${:,.2f}".format(output)})

# Netlify handler function
def handler(event, context):
    return app(event, context)
