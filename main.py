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
    pregnancies = float(request.form["pregnancies"])
    glucose = float(request.form["glucose"])
    bloodpressure = float(request.form["bloodpressure"])
    skinthickness = float(request.form["skinthickness"])
    insulin = float(request.form["insulin"])
    bmi = float(request.form["bmi"])
    age = float(request.form["age"])

    features = np.array([[pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, age]])

    prediction = model.predict(features)[0]

    if prediction == 0:
        return render_template("index.html",predicted_text="You are safe")
    if prediction == 1:
        return render_template("index.html",predicted_text="You need treatment for diabetes")
    
if __name__ == "__main__":
    app.run(debug=True)