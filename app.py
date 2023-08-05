from flask import Flask,render_template,request
import pickle
import  numpy as np

model=pickle.load(open('model.pkl','rb'))
app=Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    cgpa=float(request.form.get('cgpa'))
    iq = int(request.form.get('iq'))

    # result = model.predict(np.array((cgpa, iq)).reshape(1, 2))
    result=model.predict([[cgpa,iq]])[0]
    if result==1:
        return render_template('index.html',label=1)
    else:
        return render_template('index.html', label=-1)



if __name__=='__main__':
    app.run(debug=True)