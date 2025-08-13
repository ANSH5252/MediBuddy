# 🩺 MediBuddy: Disease Prediction System ⚕️

**MediBuddy** is a machine learning-based web application that predicts possible diseases based on symptoms selected by the user.  
It uses a trained classification model built with **Python** and **Scikit-learn**, and is served via a **Flask** web interface for an easy and interactive user experience.

## 🚀 Features

- **Symptom-based Disease Prediction** — Select multiple symptoms and get the most probable disease instantly.
- **Machine Learning Model** — Trained on a curated dataset for accurate predictions.
- **User-friendly Web Interface** — Built with HTML, CSS, and Bootstrap for a clean and responsive design.
- **Data-driven** — Uses real-world symptom–disease mapping for informed results.

## 📊 Tech Stack

**Language:** Python 🐍 , HTML , CSS 

**Libraries:**
- `pandas`, `numpy` — Data manipulation and analysis
- `scikit-learn` — Model training and prediction
- `Flask` — Web framework for the application
- `pickle` — Model serialization

**Techniques Used:**
- Classification Algorithms
- Web Development with Flask
- Form-based user input handling

## 🧠 How It Works

- Data Preprocessing — Reads and cleans the dataset (dataset.csv) containing diseases and their associated symptoms.

- Model Training — Uses classification algorithms to map symptoms to probable diseases.
  The trained model is saved as model.pkl.

- Prediction Workflow —

  - User selects symptoms via the web interface.

  - The Flask backend loads the trained model.

  - The model predicts the most likely disease.

  - The prediction is displayed to the user.

- Frontend — Built with HTML, Bootstrap, and CSS for a responsive experience.

