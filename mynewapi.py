import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('logregmodel.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    generalhealth = request.form['generalhealth']
    if(generalhealth=='Excellent'):
        generalhealth = 4
    elif(generalhealth=='Very good'):
        generalhealth = 3
    elif(generalhealth=='Good'):
        generalhealth = 2
    elif(generalhealth=='Fair'):
        generalhealth = 1
    else:
        generalhealth = 0
    sex = request.form['sex']
    if(sex=='Male'):
        sex = 1
    else:
        sex = 0
    diffwalking = request.form['diffwalking']
    if(diffwalking=='Yes'):
        diffwalking = 1
    else:
        diffwalking = 0
    smoking = request.form['smoking']
    if(smoking=='Yes'):
        smoking = 1
    else:
        smoking = 0
    alcoholdrinking = request.form['alcoholdrinking']
    if(alcoholdrinking=='Yes'):
        alcoholdrinking = 1
    else:
        alcoholdrinking = 0
    stroke = request.form['stroke']
    if(stroke=='Yes'):
        stroke = 1
    else:
        stroke = 0
    stroke = request.form['stroke']
    if(stroke=='Yes'):
        stroke = 1
    else:
        stroke = 0
    diabetic = request.form['diabetic']
    if(diabetic=='Yes'):
        diabetic = 1
    else:
        diabetic = 0
    asthma = request.form['asthma']
    if(asthma=='Yes'):
        asthma = 1
    else:
        asthma = 0
    kidneydisease = request.form['kidneydisease']
    if(kidneydisease=='Yes'):
        kidneydisease = 1
    else:
        kidneydisease = 0
    skincancer = request.form['skincancer']
    if(skincancer=='Yes'):
        skincancer = 1
    else:
        skincancer = 0
    physicalactivity = request.form['physicalactivity']
    if(physicalactivity=='Yes'):
        physicalactivity = 1
    else:
        physicalactivity = 0
        
    arr = np.array([[generalhealth,sex,diffwalking,smoking,alcoholdrinking,stroke,diabetic,asthma,kidneydisease,skincancer,physicalactivity]])
    
    age = request.form['age']
    if(age == '25-29'):
        arr1 = np.array([[1,0,0,0,0,0,0,0,0,0,0,0,]])
    elif(age == '30-34') :
        arr1 = np.array([[0,1,0,0,0,0,0,0,0,0,0,0,]])
    elif(age == '35-39') :
        arr1 = np.array([[0,0,1,0,0,0,0,0,0,0,0,0,]])
    elif(age == '40-44') :
        arr1 = np.array([[0,0,0,1,0,0,0,0,0,0,0,0,]])
    elif(age == '45-49') :
        arr1 = np.array([[0,0,0,0,1,0,0,0,0,0,0,0,]])
    elif(age == '50-54') :
        arr1 = np.array([[0,0,0,0,0,1,0,0,0,0,0,0,]])
    elif(age == '55-59') :
        arr1 = np.array([[0,0,0,0,0,0,1,0,0,0,0,0,]])
    elif(age == '60-64') :
        arr1 = np.array([[0,0,0,0,0,0,0,1,0,0,0,0,]])
    elif(age == '65-69') :
        arr1 = np.array([[0,0,0,0,0,0,0,0,1,0,0,0,]])
    elif(age == '70-74') :
        arr1 = np.array([[0,0,0,0,0,0,0,0,0,1,0,0,]])
    elif(age == '75-79') :
        arr1 = np.array([[0,0,0,0,0,0,0,0,0,0,1,0,]])
    else:
        arr1 = np.array([[0,0,0,0,0,0,0,0,0,0,0,1,]])
    
    race = request.form['race']
    if(race=='Asian'):
        arr2 = np.array([[1,0,0,0,0]])
    elif(race=='Black'):
        arr2 = np.array([[0,1,0,0,0]])
    elif(race=='Black'):
        arr2 = np.array([[0,0,1,0,0]])
    elif(race=='Black'):
        arr2 = np.array([[0,0,0,1,0]])
    else:
        arr2 = np.array([[0,0,0,0,1]])
    
    final_arr = np.concatenate((arr,arr1,arr2),axis=1)
    print(final_arr,flush=True)
    pred = model.predict(final_arr)
    

    
    return render_template('prediction.html', data=pred)
    
if __name__ == "__main__":
    app.run(debug=True)