import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("weather.csv.txt")

df = df[['MinTemp', 'MaxTemp', 'Humidity9am', 'Humidity3pm',
         'Pressure9am', 'Pressure3pm', 'RainTomorrow']]

df.dropna(inplace=True)

le = LabelEncoder()
df['RainTomorrow'] = le.fit_transform(df['RainTomorrow'])

X = df.drop('RainTomorrow', axis=1)
y = df['RainTomorrow']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

pickle.dump(model, open("model.pkl", "wb"))

print("Model saved successfully!")
