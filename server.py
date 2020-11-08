from flask import Flask
from flask import jsonify, request
from flask_cors import CORS
from PIL import Image
from io import BytesIO
import numpy
import base64

import file_to_call_script

app = Flask(__name__)
CORS(app)

def listToDict(lst):
    arr = []
    for i in range(0, len(lst), 3):
         res_dct = {"file_name":lst[i], "label":lst[i + 1], "confidence":lst[i + 2]}
         arr.append(res_dct)
    result = {"data":arr}
    return(result)

def txtToJson(file_name):
    with open(file_name) as fh: 
        for line in fh: 
            line = line.replace("{", "")
            line = line.replace("}", "")
            line = line.replace("'", "")
            line = line.replace(":", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            line = line.replace(",", "")
            result = listToDict(line.split())
            return result

def base64toImg(base64_string):
    base64_string = base64_string.replace(base64_string[:22], '', 1) 
    imgdata = base64.b64decode(base64_string)
    filename = 'screenshot.png'
    with open(filename, 'wb') as f:
        f.write(imgdata)


@app.route('/')
def home():
    return ('hello!')

# @app.route('/labels')
# def home():
#     return txtToJson('dictionaryOfResults.txt')

#\ Takes in base64 string, runs bash script, and returns results
@app.route('/saveImg', methods=['POST']) #GET requests will be blocked
def saveImg():
    req_data = request.get_json()
    base64str = req_data['base64str']
    base64toImg(base64str)
    file_to_call_script.callBashScript()
    
    return txtToJson('dictionaryOfResults.txt')

if __name__ == '__main__':
    app.run(port=8000)