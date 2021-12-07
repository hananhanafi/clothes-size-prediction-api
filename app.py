import json
from flask import Flask, request, jsonify, render_template, send_from_directory
import pickle
app = Flask(__name__)
loaded_model = pickle.load(open('finalized_model.sav', 'rb'))  # load model


@app.route('/predict/', methods=['POST'])
def get_prediction():
    req_json = json.loads(request.data)  # read request
    age = int(req_json['age'])
    weight = int(req_json['weight'])
    height = int(req_json['height'])
    bmi = weight/((height/100)**2)  # BMI Calculation
    x = [[weight, age, height, bmi]]  # Save array of request data into variable x
    result = loaded_model.predict(x)  # predict
    result_str = [str(i) for i in result]  # save the result
    return jsonify({'output': result_str})  # return model output


# A welcome message to test our server
@app.route('/')
def index():
    # return "<h1>Welcome to our server !!</h1>"
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

