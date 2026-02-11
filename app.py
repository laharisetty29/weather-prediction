from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['MinTemp']),
            float(request.form['MaxTemp']),
            float(request.form['Humidity9am']),
            float(request.form['Humidity3pm']),
            float(request.form['Pressure9am']),
            float(request.form['Pressure3pm'])
        ]

        prediction = model.predict([features])

        result = "Rain Expected ☔" if prediction[0] == 1 else "No Rain ☀"

        return render_template('index.html', prediction_text=result)

    except:
        return render_template('index.html', prediction_text="Invalid Input")

if __name__ == "__main__":
    app.run(debug=True)
