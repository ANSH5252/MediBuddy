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

## 🖥️ How to Run Locally

1️⃣ **Clone the repository**  
```
git clone https://github.com/ANSH5252/MediBuddy.git
cd MediBuddy
```
2️⃣ **Install dependencies**
```
pip install -r requirements.txt
```
3️⃣ **Start the Flask server**
- Open the **Terminal** in **Visual Studio Code** then **Paste** the follwing command and hit **Enter** .
```
python main.py
```
4️⃣ **Open in Browser**
```
http://127.0.0.1:5000/
```

---

## 🔍 How It Works

1️⃣ Data Preprocessing

- Handle missing values

- Encode categorical data

- Normalize features

2️⃣ Model Training

- Models tested:

  - Support Vector Classifier ✅ (Best performer)

  - Random Forest Classifier

  - Naive Bayes

  - XGBoost

3️⃣ Evaluation

- Accuracy calculated for each model

- SVC chosen for deployment

4️⃣ Prediction

- Input: List of symptoms

- Output: Predicted disease + severity + recommended actions
---

## 🧪 Example Usage

- Open the web app in a browser.

- Select one or multiple symptoms from the UI.

- Click Predict.

- See predicted disease, severity, and recommendations instantly.

- Check the Video Demo .


---

## 📸 Screenshots


- **Symptoms Selection Page**


<img width="1920" height="1080" alt="Pic1" src="https://github.com/user-attachments/assets/8f06ad86-f8c2-4111-a779-61127f3a5c68" />

<img width="1920" height="1080" alt="Pic2" src="https://github.com/user-attachments/assets/cd1598fa-dd0a-4a0a-9d30-b58feb88c724" />


- **Diagnosis Result Page**


<img width="1920" height="1080" alt="Pic3" src="https://github.com/user-attachments/assets/f1ec3db5-6484-4332-b5a7-e13aeab62a44" />

<img width="1920" height="1080" alt="Pic4" src="https://github.com/user-attachments/assets/84886bc2-2bf7-4b86-9613-2c736a1d5c18" />


- **About Page**

  
<img width="1920" height="1080" alt="Pic5" src="https://github.com/user-attachments/assets/018af514-4795-4c4b-9a84-ea81880f1aaf" />


- **Contact Page**


<img width="1920" height="1080" alt="Pic6" src="https://github.com/user-attachments/assets/8e42b78a-a25f-4e42-9379-d53f281eff6f" />


- **Developer Page**


<img width="1920" height="1080" alt="Pic7" src="https://github.com/user-attachments/assets/5137fb5e-c3f6-40f0-8662-ca779492d02e" />


- **Blog Page**


<img width="1920" height="1080" alt="Pic8" src="https://github.com/user-attachments/assets/702a90fb-1a54-473c-84e0-c6a6566111de" />


- **MediBuddy Walkthrough**



---

## 💡 Future Enhancements

- Integrate real-time health monitoring from wearable devices

- Multi-language support for a wider audience

- Deploy on cloud platforms for global access

- Include an AI chat assistant for personalized medical advice
---

## 🤝 Contributing

Contributions and feedback are welcome!

- Fork the repository

- Create a new feature branch

- Commit your changes

- Submit a pull request 🚀

---

## ⭐ If You Liked This Project

Please consider giving it a 🌟 Star on GitHub! It helps a lot.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Anshuman Dash**   

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/ANSH5252) 

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/anshuman-dash-739793351/)
