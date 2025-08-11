# Import Flask and other necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import the CORS library
import numpy as np
import pandas as pd
import pickle
import warnings
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import os

# Suppress all warnings
warnings.filterwarnings("ignore")

# Initialize the Flask app
app = Flask(__name__)
# Enable CORS for all routes
CORS(app)

# =============================================================
# Load Datasets and Model (This runs once when the app starts)
# =============================================================

try:
    # Get the base directory for the Flask app
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full paths to the data files
    data_dir = os.path.join(base_dir, 'data')
    models_dir = os.path.join(base_dir, 'models')

    # Load the datasets
    df = pd.read_csv(os.path.join(data_dir, 'Training.csv'))
    symptom_severity = pd.read_csv(os.path.join(data_dir, 'Symptom-severity.csv'))
    precautions = pd.read_csv(os.path.join(data_dir, 'precautions_df.csv'))
    workout = pd.read_csv(os.path.join(data_dir, 'workout_df.csv'))
    description = pd.read_csv(os.path.join(data_dir, 'description.csv'))
    medications = pd.read_csv(os.path.join(data_dir, 'medications.csv'))
    diets = pd.read_csv(os.path.join(data_dir, 'diets.csv'))

    # Load the trained SVC model
    with open(os.path.join(models_dir, 'svc.pkl'), 'rb') as model_file:
        svc = pickle.load(model_file)

    # Recreate the dictionaries and lists needed for prediction
    symptoms_list = df.columns[:-1].tolist()
    symptoms_dict = {symptom: index for index, symptom in enumerate(symptoms_list)}
    
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(df['prognosis'])
    
    # Create the disease mapping
    temp_df = pd.DataFrame(y_encoded, columns=['prognosis_encoded'])
    temp_df['prognosis'] = df['prognosis']
    temp_df.drop_duplicates(keep='first', inplace=True)
    diseases_list = temp_df.set_index('prognosis_encoded')['prognosis'].to_dict()

    # Pre-process the workout data
    workout_rows = []
    for i in range(0, len(workout), 10):
        disease = workout['disease'].iloc[i]
        workout_list = workout['workout'].iloc[i:i+10].tolist()
        workout_rows.append({'disease': disease, 'workout': workout_list})
    workout_new = pd.DataFrame(workout_rows)
    print("Successfully loaded model and data.")

except FileNotFoundError as e:
    print(f"Error loading files: {e}")
    print("Make sure 'data' and 'models' folders exist and contain the required files.")
    exit()

# =============================================================
# Helper Functions for Prediction
# =============================================================

def fetch_prediction(user_symptoms):
    """Predicts the disease based on user-provided symptoms."""
    # Create a zero-filled numpy array for all possible symptoms
    input_data = np.zeros(len(symptoms_dict))

    # For each symptom provided by the user, set its corresponding index to 1
    for symptom in user_symptoms:
        if symptom in symptoms_dict:
            input_data[symptoms_dict[symptom]] = 1

    # Predict the disease using the SVC model
    pred_index = svc.predict([input_data])[0]
    return diseases_list.get(pred_index, "Unknown Disease")

def fetch_description(disease):
    """Fetches the description for a given disease."""
    if disease in description['Disease'].values:
        return description[description['Disease'] == disease]['Description'].values[0]
    return "Description not found."

def fetch_precautions(disease):
    """Fetches the precautions for a given disease."""
    if disease in precautions['Disease'].values:
        return precautions[precautions['Disease'] == disease][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values[0].tolist()
    return ["Precautions not found."]

def fetch_medications(disease):
    """Fetches the medications for a given disease."""
    if disease in medications['Disease'].values:
        fetched_medications = medications[medications['Disease'] == disease]['Medication'].values[0]
        # Use a safe method to evaluate the string representation of a list
        return eval(fetched_medications) 
    return ["Medications not found."]

def fetch_diet(disease):
    """Fetches the diet recommendations for a given disease."""
    if disease in diets['Disease'].values:
        fetched_diet = diets[diets['Disease'] == disease]['Diet'].values[0]
        return eval(fetched_diet)
    return ["Diets not found."]

def fetch_workout(disease):
    """Fetches the workout recommendations for a given disease."""
    if disease in workout_new['disease'].values:
        return workout_new[workout_new['disease'] == disease]['workout'].values[0]
    return ["Workout not found."]

def fetch_symptoms_severity_level(symptom_list):
    """Calculates the symptom severity level."""
    total_severity = 0
    count = 0
    for s in symptom_list:
        if s in symptom_severity['Symptom'].values:
            severity = symptom_severity[symptom_severity['Symptom'] == s]['weight'].values[0]
            total_severity += severity
            count += 1
    
    if count == 0:
        return "No valid symptoms found.", 0.0

    rounded_value = round(np.float64(total_severity / count), 2)
    
    if rounded_value < 2.99:
        severity_level = "Mild"
    elif rounded_value < 4.99:
        severity_level = "Moderate"
    else:
        severity_level = "Severe"
    
    return severity_level, rounded_value

def clean_symptom_name(symptom_name):
    """Cleans up a symptom name to match the dataset format."""
    return symptom_name.strip().replace(' ', '_')

# =============================================================
# Flask Routes
# =============================================================

@app.route('/')
def home():
    """Renders the main home page."""
    return render_template('index.html', active_page='home')

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html', active_page='about')

@app.route('/blog')
def blog():
    """Renders the blog page."""
    return render_template('blog.html', active_page='blog')

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html', active_page='contact')

@app.route('/developer')
def developer():
    """Renders the developer page."""
    return render_template('developer.html', active_page='developer')

@app.route('/process_symptoms', methods=['POST'])
def process_symptoms():
    """API endpoint to receive symptoms and return a diagnosis."""
    data = request.get_json()
    user_symptoms = data.get('symptoms', [])
    
    if not user_symptoms:
        return jsonify({
            'status': 'error',
            'message': 'No symptoms provided.'
        }), 400

    # Clean the symptom names to match the format in the ML model
    cleaned_symptoms = [clean_symptom_name(symptom) for symptom in user_symptoms]
    
    # Get the diagnosis and other related information
    diagnosis = fetch_prediction(cleaned_symptoms)
    description = fetch_description(diagnosis)
    precautions = fetch_precautions(diagnosis)
    medications = fetch_medications(diagnosis)
    diet = fetch_diet(diagnosis)
    workout = fetch_workout(diagnosis)
    severity_level, severity_score = fetch_symptoms_severity_level(cleaned_symptoms)

    # Return all the information as a single JSON object
    return jsonify({
        'status': 'success',
        'diagnosis': diagnosis,
        'description': description,
        'precautions': precautions,
        'medications': medications,
        'diet': diet,
        'workout': workout,
        'severity_level': severity_level,
        'severity_score': severity_score
    })

if __name__ == "__main__":
    app.run(debug=True)
