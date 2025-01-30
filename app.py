import json  # for parsing JSON data
import pickle  # for serializing and deserializing Python objects

from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd

# Initializing Flask app
app = Flask(__name__)

# Load model and scaler
regmodel = pickle.load(open('regmodel.pkl', 'rb'))  # Load regression model
scaler = pickle.load(open('scaling.pkl', 'rb'))  # Load scaler object for data normalization

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        # Extract JSON data from request
        data = request.json['data']
        print("Received JSON Data:", data)

        # Convert data values into numpy array and reshape to match model input
        input_data = np.array(list(data.values())).reshape(1, -1)
        print("Input Array:", input_data)

        # Normalize the input data
        new_data = scaler.transform(input_data)

        # Predict output using the loaded regression model
        output = regmodel.predict(new_data)[0]
        print("Predicted Output:", output)

        # Return prediction as JSON response
        return jsonify({"prediction": float(output)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form values from POST request and convert them to float
        data = [float(x) for x in request.form.values()]

        # Normalize the data using the loaded scaler
        final_input = scaler.transform(np.array(data).reshape(1, -1))

        # Predict output using the loaded regression model
        output = regmodel.predict(final_input)[0]

        # Render home.html template with prediction text
        return render_template("home.html", predict_text="The house price prediction is ${:,.2f}".format(output))

    except Exception as e:
        return render_template("home.html", predict_text=f"Error: {str(e)}")

# Netlify Lambda function handler
def handler(event, context):
    return app(event, context)

if __name__ == "__main__":
    app.run(debug=True)
