from flask import Flask, request,jsonify
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/predict',methods=['POST'])
def predict():
    glucose=request.form.get('glucose')
    bloodPressure=request.form.get('bloodPressure')
    skinThickness=request.form.get('skinThickness')
    insulin=request.form.get('insulin')
    bmi=request.form.get('bmi')
    age=request.form.get('age')

    input_query=np.array([[glucose,bloodPressure,skinThickness,insulin,bmi,age]])
    result=model.predict(input_query)[0]
    #result={'glucose':glucose,'bloodPressure':bloodPressure,'skinThickness':skinThickness,'insulin':insulin,'bmi':bmi,'dpf':dpf,'age':age}
    return jsonify({'risk_level':str(result)})

if __name__=='__main__':
    app.run(debug=True)
