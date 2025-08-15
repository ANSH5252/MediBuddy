# 🩺 MediBuddy – AI-Powered Health Companion

**MediBuddy** is an **AI-powered web application** that predicts possible diseases based on selected symptoms and provides **complete health guidance** — including precautions, medications, recommended diets, and workouts. Built with **Python, Flask, Bootstrap, and Machine Learning models** for a smooth and interactive experience.

---

## 🚀 Features

- 🔍 **Symptom-based Prediction**: Enter one or more symptoms and get the most probable disease using a trained ML model.  
- 📊 **Multiple Health Datasets**: Includes disease descriptions, symptom severity, medications, diet plans, workouts, and precautions.  
- 🤖 **AI Model Selection**: Various models tested (SVC, RandomForest, Naive Bayes, XGBoost) → **SVC chosen** for best accuracy.  
- ⚡ **Severity Calculation**: Determines how critical the symptoms are and provides urgency levels.  
- 💡 **Comprehensive Guidance**: Detailed info including disease description, precautions, medications, diet, and exercise tips.  
- 🖥️ **User-Friendly Interface**: Responsive Bootstrap design for smooth navigation and quick symptom selection.  

---

## 🧰 Tech Stack

- **Language:** Python 🐍  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **Backend:** Flask  
- **Machine Learning:** scikit-learn, XGBoost  
- **Data Handling:** pandas, NumPy  
- **Model Persistence:** pickle  
- **Other Tools:** Jupyter Notebook, Git  

**Techniques Used:**  
- Feature Encoding & Normalization  
- Severity Scoring  
- Model Training & Evaluation  
- Prediction with Detailed Recommendations  

---

## 🗂 Project Structure
```
MediBuddy/
│
├── main.py                   # Flask backend entry point
├── mb.ipynb                  # ML training & evaluation notebook
│
├── static/                   # Static files (CSS, JS, images)
│   └── style.css             # Custom CSS styling
│
├── templates/                # HTML templates
│   ├── base.html             # Main layout
│   ├── index.html            # Symptom selection UI
│   ├── about.html            # About MediBuddy
│   ├── blog.html             # Journey of building MediBuddy
│   ├── contact.html          # Contact details
│   └── developer.html        # About the developer
│
├── data/                     # Datasets used in the project
│   ├── Training.csv          # Dataset for model training
│   ├── symptoms_df.csv       # Symptoms of different diseases
│   ├── Symptom-severity.csv  # Severity levels for symptoms
│   ├── description.csv       # Disease descriptions
│   ├── medications.csv       # Medications for different diseases
│   ├── diets.csv             # Diet recommendations per disease
│   ├── workout_df.csv        # Workouts per disease
│   └── precautions.csv       # Precautionary measures for diseases
│
├── models/                   # Trained machine learning models
│   └── svc.pkl               # Trained SVC model
│
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies
```
---
