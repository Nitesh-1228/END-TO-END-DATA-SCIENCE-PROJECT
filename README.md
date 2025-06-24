# END-TO-END-DATA-SCIENCE-PROJECT
COMPANY: CODTECH IT SOLUTIONS

NAME: IPPILI NITESH

INTERN ID: CT06DL1202

DOMAIN: DATA SCIENCE

DURATION: 6 WEEKS

MENTOR: NEELA SANTHOSH
# DESCRIPTION
In this project, a complete end-to-end data science workflow is implemented to predict the likelihood of diabetes based on medical input features. The process includes data preprocessing, model training, saving the model, and deploying a Flask web application that serves predictions in real-time.

This task meets the requirement of building a deployed API/web app for model interaction, as specified in the internship deliverables.

Steps Performed
Step 1: Data Preprocessing & Model Training

The Pima Indians Diabetes Dataset was used.Zero values in medical features like Glucose, BloodPressure, and BMI were treated as missing and imputed using the mean strategy.Features were scaled using StandardScaler to ensure proper model performance.A Random Forest Classifier was trained on the cleaned data and saved using joblib for later deployment.

Step 2: Web App with Flask
A Flask web application (app.py) was created to serve the model.The user interface was designed using HTML (templates/index.html) to collect user inputs.Inputs are processed and scaled before being passed to the trained model for prediction.The result (Diabetic / Not Diabetic) is displayed on the same web page.

How to Run Locally
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Ensure Files are Present

diabetes_model.pkl — Trained model file

scaler.pkl — Scaler object

app.py — Flask application

templates/index.html — HTML form

Open Browser
Visit http://127.0.0.1:5000/ and enter details in the form to get predictions.

# OUTPUT

![Image](https://github.com/user-attachments/assets/df169083-95dc-4eee-b0c8-24f9a0591b46)

![Image](https://github.com/user-attachments/assets/9ce902ac-c1ce-4bfb-ad48-69bf15ffe642)

![Image](https://github.com/user-attachments/assets/bf901c0d-6a9b-4f55-88da-ebe25e0b1a4c)

