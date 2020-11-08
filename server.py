from flask import Flask
from flask import jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

import test

@app.route('/')
def home():
    return "Mask Detection API!"

@app.route('/capture')
def capture():
    #take the screenshot from the screenshot file
    #feed that into the python file that does image processing
    #return the faces
    return test.hello()

@app.route('/predict')
def predict():
    #run function that tests the images found in the tests folder, returns dict
    return jsonify("one")


if __name__ == '__main__':
    app.run(port=8000)