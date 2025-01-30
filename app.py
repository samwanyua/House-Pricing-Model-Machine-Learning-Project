import os
import json  # for parsing JSON data
import pickle  # for serializing and deserializing Python Objects
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd

# Initializing Flask app
app = Flask(__name__)

# Load model and scaler
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scalar.transform(np.array(data).reshape(1, -1))
    print(final_input)
    output = regmodel.predict(final_input)[0]
    return render_template("home.html", predict_text="The house prediction is ${:,.2f}".format(output))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway assigns a port dynamically
    app.run(debug=True, host="0.0.0.0", port=port)
