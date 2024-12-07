import json # for parsing JSON data
import pickle # for serializing and deserializing Python Objects

from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd 

# Initializing flask app
app=Flask(__name__)

# load model
regmodel=pickle.load(open('regmodel.pkl','rb')) # loads regression model
scalar = pickle.load(open('scaling.pkl','rb')) # loads scaler object for data normalization

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    # extract JSON data from request
    data= request.json['data'] 
    print(data)
    # convert data values into numpy array and reshape it to match model's expected input
    print(np.array(list(data.values())).reshape(1, -1))
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    # predict output using the loaded regression model
    output = regmodel.predict(new_data)
    print(output[0])
    # return prediction as a JSON response
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])
def predict():
    # extract form values from POST request and convert them to float
    data=[float(x) for x in request.form.values()]
    # normalize the data using the loaded scaler
    final_input= scalar.transform(np.array(data).reshape(1, -1))
    print(final_input)
    # predict output using the loaded regression
    output= regmodel.predict(final_input)[0]
    # render home.html template with prediction text
    return render_template("home.html", predict_text="The house prediction is ${:,.2f}".format(output))

if __name__=="__main__":
    app.run(debug=True)