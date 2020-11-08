from flask import Flask
from flask import jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

from PIL import Image
import cv2
import numpy
import base64
import test
from io import BytesIO
import np
import sys


def base64toImg(base64_string):
    print('asdf')
    base64_string = base64_string.replace(base64_string[:22], '', 1) 
    imgdata = base64.b64decode(base64_string)
    filename = 'some_image.png'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    # f gets closed when you exit the with statement
    # Now save the value of filename to your database

@app.route('/')
def home():
    print('bb')
    print('Hello world!', file=sys.stderr)
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

#Recieve base 64 str
@app.route('/saveImg', methods=['POST']) #GET requests will be blocked
def saveImg():
    req_data = request.get_json()
    print('Hello world!', file=sys.stderr)
    base64str = req_data['base64str']
    base64toImg(base64str)
    return jsonify("success")

if __name__ == '__main__':
    app.run(port=8000)