import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv("diabetes.csv")

if not os.path.exists("model.pkl"):
    
    df.drop(['DiabetesPedigreeFunction'], axis=1, inplace=True)

    X = df[['Pregnancies',	'Glucose',	'BloodPressure',	'SkinThickness',	'Insulin',	'BMI',	'Age']]
    y = df['Outcome']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = GaussianNB()
    clf.fit(X_train,y_train)

    joblib.dump(clf,"model.pkl")
    print("Model trained and saved as model.pkl")

else:
    print("You already have model.pkl file so,\nRun command : python ./main.py")