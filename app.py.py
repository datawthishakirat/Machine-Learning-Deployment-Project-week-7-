#!/usr/bin/env python
# coding: utf-8

# # Run API

# In[ ]:


from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load saved model
model = joblib.load('housing_model.pkl')

@app.route('/')
def home():
    return "Housing Price Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json

    input_data = pd.DataFrame([data])

    prediction = model.predict(input_data)

    return jsonify({
        'Predicted Price': float(prediction[0])
    })

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)


# In[ ]:




