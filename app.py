import pickle
from flask import Flask, request, render_template, jsonify

model = pickle.load(open('model.pkl', 'rb'))
label_encoders = pickle.load(open('encoders.pkl', 'rb'))
stage_encoder = pickle.load(open('stage_encoder.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Main prediction page

@app.route('/details')
def details():
    return render_template('details.html')  # Info/education page

@app.route('/contact')
def contact():
    return render_template('details.html')

@app.route("/predict-page")
def predict_page():
    return render_template("predict.html")

@app.route('/predict', methods=['POST'])
def predict():
    input_data = [
        request.form['Gender'],
        request.form['Age'],
        request.form['History'],
        request.form['Patient'],
        request.form['TakeMedication'],
        request.form['Severity'],
        request.form['BreathShortness'],
        request.form['VisualChanges'],
        request.form['NoseBleeding'],
        request.form['Whendiagnoused'],
        request.form['Systolic'],
        request.form['Diastolic'],
        request.form['ControlledDiet']
    ]

    columns = list(label_encoders.keys())
    encoded_input = [label_encoders[col].transform([val])[0] for col, val in zip(columns, input_data)]
    prediction = model.predict([encoded_input])[0]
    predicted_stage = stage_encoder.inverse_transform([prediction])[0]

    return render_template('result.html', prediction=f"Predicted Stage: {predicted_stage}")

if __name__ == '__main__':
    app.run(debug=True)
