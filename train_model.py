import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv("diabetes.csv")

if not os.path.exists("model.pkl"):
    
    X = df.drop(['Outcome', 'DiabetesPedigreeFunction'], axis=1)
    y = df['Outcome']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    num_features = X.select_dtypes(exclude='object').columns
    
    num_transformer = Pipeline(steps=[
    ('scaling', StandardScaler())
    ])

    preprocessor = ColumnTransformer(transformers=[
    ('num', num_transformer, num_features)
    ], remainder='drop')

    model = GaussianNB()

    final_model = Pipeline(steps=[
    ('preprocesssing', preprocessor),
    ('model', model)
    ])
    
    final_model.fit(X_train,y_train)

    joblib.dump(final_model,"model.pkl")
    
    print("Model trained and saved as model.pkl")

else:
    print("You already have model.pkl file so,\nRun command : python ./main.py")
