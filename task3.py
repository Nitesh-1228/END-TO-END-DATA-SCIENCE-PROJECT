import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Load and clean dataset
df = pd.read_csv("diabetes.csv")
invalid_cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[invalid_cols] = df[invalid_cols].replace(0, np.nan)
imputer = SimpleImputer(strategy='mean')
df[invalid_cols] = imputer.fit_transform(df[invalid_cols])

X = df.drop('Outcome', axis=1)
y = df['Outcome']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)
joblib.dump(rf, 'diabetes_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

# STEP 2: Flask App (app.py)
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('diabetes_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_input = scaler.transform([features])
    prediction = model.predict(final_input)
    result = 'Diabetic' if prediction[0] == 1 else 'Not Diabetic'
    return render_template('index.html', prediction_text=f'Result: {result}')

if __name__ == "__main__":
    app.run(debug=True)