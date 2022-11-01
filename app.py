from flask import Flask, render_template, request
app = Flask(__name__)
import pickle
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "mNchOQo_3dIJ3QGdbWaZbzeCZ3lB8b1bg85GI1c7s647"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


model = pickle.load(open('assets/randomforest_frog.pkl','rb'))


@app.route('/')
def helloworld():
    sites = ['Pollinator','Indicator']
    return render_template("base.html",sites=sites)
@app.route('/assesment')
def prediction():
    return render_template("index1.html")

@app.route('/risk', methods = ['POST'])
def admin():
    return render_template("index2.html")
    #  gather = request.form["site"]
    #  print(gather)
    #  if (gather == "Pollinator"):
    #     return render_template("index.html")
    #  if (gather == "Indicator"):
    #     return render_template("index2.html")
        
    # y=[[int(p),int(q),int(r),int(s),int(t),int(u),int(v),int(w),int(x)]]   
    # payload_scoring = {"input_data": [{"field": [["age","gender","job","housing","saving","checking","credit","duration","purpose"]], "values": y}]}     
    # # a = model.predict(y)
    # response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/344a0509-9531-413a-aa1a-509c569e1d2d/predictions?version=2022-10-20', json=payload_scoring,
    # headers={'Authorization': 'Bearer ' + mltoken})
    # predictions=response_scoring.json()
    # print(predictions['predictions'][0]['values'][0][0])
    # if (predictions['predictions'][0]['values'][0][0] == "bad"):
    #      return render_template("predbad.html", z = predictions['predictions'][0]['values'][0][0])

    # if (predictions['predictions'][0]['values'][0][0] == "good"):
    #      return render_template("predgood.html", z = predictions['predictions'][0]['values'][0][0])

if __name__ == '__main__':
    app.run(debug = True)