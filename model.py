import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# load dataset
data = pd.read_csv("dataset.csv")

# inputs and output
X = data[['CO2','SpO2','BreathingRate']]
y = data['Condition']

# train model
model = DecisionTreeClassifier()
model.fit(X, y)

# save model
joblib.dump(model, "model.pkl")

print("Model ready!")