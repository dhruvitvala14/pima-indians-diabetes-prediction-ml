import numpy as np
import joblib
from flask import Flask, request, render_template

app = Flask(__name__)

model = joblib.load("model.pkl")
print("Loaded model type:", type(model))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    import pandas as pd

    data = {
        "Pregnancies": float(request.form["pregnancies"]),
        "Glucose": float(request.form["glucose"]),
        "BloodPressure": float(request.form["bloodpressure"]),
        "SkinThickness": float(request.form["skinthickness"]),
        "Insulin": float(request.form["insulin"]),
        "BMI": float(request.form["bmi"]),
        "Age": float(request.form["age"]),
    }

    features = pd.DataFrame([data])

    prediction = model.predict(features)[0]

    if prediction == 0:
        return render_template("index.html", predicted_text="You are safe")
    else:
        return render_template("index.html", predicted_text="You need treatment for diabetes")

if __name__ == "__main__":
    app.run(debug=True)
