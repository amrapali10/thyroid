from flask import Flask,render_template,url_for,request
import pandas as pd
import pickle
import numpy as np


app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('home.html')

@app.route('/',methods=['POST'])
def predict():
    if request.method == 'POST':
        model = pickle.load(open('model.pkl','rb'))
                
        float_features = [float(x) for x in request.form.values()]
        final_features = [np.array(float_features)]
        
        #test_df = np.array([[7,31,2,0,2,1,35,5,8,0,49]])
        #pd.DataFrame({'department':"Sales & Marketing", 'region':"region_19", 'education':"Bachelor's", 'gender':"m", 'recruitment_channel':"sourcing", 'no_of_trainings':1, 'age':34, 'previous_year_rating':3, 'length_of_service':7, 'awards_won':0, 'avg_training_score':50})
        #test_df = pd.DataFrame({'department':[dept], 'region':[reg], 'education':[edu], 'gender':[gend], 'recruitment_channel':[recu], 'no_of_trainings':[train], 'age':[age], 'previous_year_rating':[prating], 'length_of_service':[lservice], 'awards_won':[award], 'avg_training_score':[tscore]})
        print(final_features)
        pred_promote = model.predict(final_features)
        #return "promotion"+pred_promote
        return render_template('result.html',prediction = pred_promote)	
    #return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)