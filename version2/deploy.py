from flask import Flask,render_template,request
import pickle

app=Flask(__name__)
model = pickle.load(open('savedModel.sav','rb'))


@app.route('/')
def home():
    result = ''
    return render_template('index.html',**locals())

@app.route('/predict', methods=['GET','POST'])
def predict():
    Age = float(request.form['Age'])
    Sex = float(request.form['Sex'])
    ChestPainType = float(request.form['ChestPainType'])
    RestingBP = float(request.form['RestingBP'])
    Cholesterol = float(request.form['Cholesterol'])
    FastingBS = float(request.form['FastingBS'])
    RestingECG = float(request.form['RestingECG'])
    MaxHR = float(request.form['MaxHR'])
    ExerciseAngina = float(request.form['ExerciseAngina'])
    Oldpeak = float(request.form['Oldpeak'])
    ST_Slope = float(request.form['ST_Slope'])
    result =  model.predict([[Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]])[0]
    if(result ==0):
        result_text=" Patient is not likely to have a heart failure."
    else:
        result_text=" Patient is likely to have a heart failure."        
    return render_template('index.html',**locals())
    

if __name__=='__main__':
    app.run(debug=True)