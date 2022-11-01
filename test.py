
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "mNchOQo_3dIJ3QGdbWaZbzeCZ3lB8b1bg85GI1c7s647"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["age","gender","job","housing","saving","checking","credit","duration","purpose"]], "values": [[67,1,1,0,2,1,200000,6,5]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/344a0509-9531-413a-aa1a-509c569e1d2d/predictions?version=2022-10-20', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions=response_scoring.json()
print(predictions)
print("val",predictions['predictions'][0]['values'][0][0])