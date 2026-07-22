# Machine-Learning-Deployment-Project-week-7-

# House Price Prediction System

## Project Description

This project is a Machine Learning-based House Price Prediction System developed as part of the AnalystLab Africa Data Science Internship Program (Week 7: Model Deployment & Real-World Application).

The system predicts house prices based on property characteristics such as area, number of bedrooms, bathrooms, stories, parking availability, location preferences and other housing features.

The trained machine learning model was saved using Joblib and deployed through a Flask API and a Streamlit web application, allowing users to generate house price predictions without retraining the model.

---

# Problem Statement

Property valuation is an important aspect of the real estate industry. Estimating house prices manually can be time-consuming and may lead to inconsistencies.

The goal of this project is to build a machine learning model capable of predicting house prices based on housing characteristics and deploy the model so users can interact with it through an API and a web application.

---

# Dataset

Dataset: Housing Prices Dataset

Target Variable:

* Price

Features:

* Area
* Bedrooms
* Bathrooms
* Stories
* Parking
* Main Road Access
* Guest Room
* Basement
* Hot Water Heating
* Air Conditioning
* Preferred Area
* Furnishing Status

Engineered Features:

* Total Rooms
* Area Per Bedroom
* Parking Availability Indicator

---

# Machine Learning Model Used

Model:

* Random Forest Regressor


# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Flask
* Streamlit
* Matplotlib
* Seaborn
* Jupyter Notebook

---

# Project Structure

```text
House-Price-Prediction/
│
├── housing_model.pkl
├── Check the saved trained model
|──app.py
|──test_api.py
├── streamlit_app.py.py
├── README.md

```

---

# API Endpoints

## Home Endpoint

URL:

```text
/
```

Method:

```text
GET
```

Response:

```text
Housing Price Prediction API is running!
```

---

## Prediction Endpoint

URL:

```text
/predict
```

Method:

```text
POST
```

Description:

Accepts housing information and returns a predicted house price.

---

# Input Format

Example JSON Request:

```json
{
  "area": 7420,
  "bedrooms": 4,
  "bathrooms": 2,
  "stories": 3,
  "parking": 2,
  "total_rooms": 6,
  "area_per_bedroom": 1855,
  "has_parking": 1,
  "luxury_home": 0,
  "mainroad_yes": 1,
  "guestroom_yes": 0,
  "basement_yes": 0,
  "hotwaterheating_yes": 0,
  "airconditioning_yes": 1,
  "prefarea_yes": 1,
  "furnishingstatus_semi-furnished": 0,
  "furnishingstatus_unfurnished": 0
}
```

---

# Output Format

Example Response:

```json
{
  "Predicted Price": 8891042.06
}
```

---


# How to Run the Flask API

Run:

```bash
python app.py
```

API will start on:

```text
http://127.0.0.1:5000
```

---

# How to Run the Streamlit Application

Run:

```bash
streamlit run streamlit_app.py
```

Application will open in your browser at:

```text
http://localhost:8501
```

---

# Project Workflow

1. Save week 6 model
2. Model Serialization using Joblib
3. API Development using Flask
4. User Interface Development using Streamlit
5. Deployment and Testing

---

# Key Lessons Learned

* Feature engineering can improve model performance by creating meaningful predictors from existing variables.
* Cross-validation helps evaluate model robustness and reduce overfitting.
* Hyperparameter tuning does not always guarantee significant performance improvements.
* Data leakage should be avoided when creating features.
* Model deployment transforms a machine learning model into a real-world application that users can interact with.

---

# Author

Shakirat Dabiri

AnalystLab Africa Data Science Internship Program – Week 7

Machine Learning | Data Science | Model Deployment | Streamlit | Flask

