from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the machine learning model
with open('payments.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/predict')
def predo():
    return render_template('/predict.html')

@app.route('/pred', methods=['POST','GET'])
def predict():
    # Get input values from the form
    step = request.form['step']
    transaction_type = request.form['type']
    amount = float(request.form['amount'])
    old_balance_org = float(request.form['oldbalanceOrg'])
    new_balance_orig = float(request.form['newbalanceOrig'])
    old_balance_dest = float(request.form['oldbalanceDest'])
    new_balance_dest = float(request.form['newbalanceDest'])

    # Preprocess the input data
    # You might need to adjust this part based on your model's requirements
    input_data = np.array([[step,transaction_type,amount, old_balance_org, new_balance_orig, old_balance_dest, new_balance_dest]])

    # Make prediction using the model
    prediction = model.predict(input_data)

    # Display the prediction result
    return render_template('/submit.html', prediction_value=str(prediction))

if __name__ == '__main__':
    app.run(debug=True)
