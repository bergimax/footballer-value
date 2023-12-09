# # LOAD A MODEL
import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = 'player_model.bin'

with open(model_file, 'rb') as f_in: 
    dv, model = pickle.load(f_in) 

app = Flask('player_value')

@app.route('/predict', methods=['POST'])

#create data to test it

def predict():
  player = request.get_json()

  X = dv.transform([player])
  y_pred = model.predict(X)

  result = {
     "curr_value": float(y_pred)
  }

  return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)