# Diabetes Prediction Using Gaussian Naive Bayes

This project builds a Machine Learning model using the **Pima Indians Diabetes Dataset** to predict the likelihood of diabetes based on medical features. A **Gaussian Naive Bayes** classifier is trained and achieves an accuracy of **74%**.  
A **Flask web app** with HTML/CSS allows users to input values and receive real-time predictions.

---

## 🚀 Features
- Gaussian Naive Bayes model for diabetes prediction  
- Flask web interface for user input and prediction  
- Clean and simple HTML/CSS UI  
- Model training script included  

---

## 🛠 Tech Stack
- Python  
- Scikit-learn  
- Pandas / NumPy  
- Flask  
- HTML / CSS  

---

## 📂 Project Structure
project/
│── main.py # Flask application
│── train_model.py # Model training script
│── diabetes.csv # Dataset
│── model.pkl # Trained model file
│
├── templates/
│ └── index.html # Web interface
│
├── static/
│ └── style.css # Stylesheet
│
└── screenshot/
└── home.png # App UI screenshot

---

## 🔧 How to Run

### 1. Install required packages
pip install -r requirements.txt

### 2. Train the model
python train_model.py


### 3. Start the Flask server
python main.py


Open the app in your browser:  
**http://127.0.0.1:5000/**

---

## 📊 Model Performance
- **Algorithm:** Gaussian Naive Bayes  
- **Accuracy:** ~74%  

---

## 📸 Screenshot
See: `/screenshot/home.png`

---

## 🤝 Contributions
Contributions and suggestions are welcome!

---

## 📜 License
This project is open-source.
