import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
app = Flask(__name__)
CORS(app)
loaded_model = pickle.load(open('finalized_model.sav', 'rb'))  # load model


@app.route('/predict/', methods=['POST'])
def get_prediction():
    req_json = json.loads(request.data)  # read request
    age = req_json['age']
    weight = req_json['weight']
    height = req_json['height']
    bmi = req_json['weight']/((req_json['height']/100)**2)  # BMI Calculation
    x = [[weight, age, height, bmi]]  # Save array of request data into variable x
    result = loaded_model.predict(x)  # predict
    result_str = [str(i) for i in result]  # save the result
    return jsonify({'output': result_str})  # return model output


# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    app.run()

