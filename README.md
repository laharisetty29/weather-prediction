# 🌦 Rain Prediction System (Machine Learning + Flask)

An end-to-end Weather Prediction Web Application that predicts whether it will rain tomorrow based on weather parameters using Machine Learning.

---

## 🚀 Project Overview

This project uses a Random Forest Classification model trained on weather data to predict rainfall.  
The trained model is deployed using Flask as a web application where users can input weather conditions and get real-time predictions.

---

## 🧠 Machine Learning Workflow

- Data preprocessing
- Handling missing values
- Label encoding
- Train-test split
- Random Forest Classifier
- Model evaluation using accuracy score
- Model serialization using Pickle

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML / CSS
- Git & GitHub

---

## 📂 Project Structure

weather_prediction/
│
├── app.py
├── train_model.py
├── weather.csv
├── model.pkl
├── requirements.txt
├── templates/
│ └── index.html
└── README.md


---


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/weather-prediction-ml.git
cd weather-prediction

###2️⃣ Create Virtual Environment
```bash
python -m venv venv
###3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
###🧪 Run Model Training
```bash
python train_model.py
This will generate:```bash model.pkl

###🌐 Run Flask App
```bash
python app.py
Open browser:```bash http://127.0.0.1:5000/

###📊 Sample Input

| Feature     | Example |
| ----------- | ------- |
| MinTemp     | 15      |
| MaxTemp     | 31      |
| Humidity9am | 85      |
| Humidity3pm | 45      |
| Pressure9am | 1008    |
| Pressure3pm | 1005    |

###🎯 Output
Rain Expected ☔
No Rain ☀

---

Deployed by Lahari Gadamsetty




