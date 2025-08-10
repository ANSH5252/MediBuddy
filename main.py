from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', active_page='home')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

@app.route('/blog')
def blog():
    return render_template('blog.html', active_page='blog')

@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')

@app.route('/developer')
def developer():
    return render_template('developer.html', active_page='developer')

@app.route('/process_symptoms', methods=['POST'])
def process_symptoms():
    data = request.get_json()
    symptoms = data.get('symptoms', [])
    # Add your symptom processing logic here

    return jsonify({
        'status': 'success',
        'message': 'Symptoms received',
        'received_symptoms': symptoms,
        'diagnosis': 'Sample diagnosis result'
    })

if __name__ == "__main__":
    app.run(debug=True)