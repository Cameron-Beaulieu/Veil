# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""label_image for tflite."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import time
import os

import numpy as np
from PIL import Image
import tensorflow as tf  # TF2

def assignLabelToImage (dictionaryOfValuesandLabels):
  highestPercentage = 0
  highestLabel = ""
  for key in dictionaryOfValuesandLabels:
    if dictionaryOfValuesandLabels[key] > highestPercentage:
      highestPercentage = dictionaryOfValuesandLabels[key]
      highestLabel= key
  return highestLabel
  
def load_labels(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]


def classifyImages():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--tests", default="tests", help="folder of test images to be classified"
    )
    parser.add_argument(
        "-m",
        "--model_file",
        default="/tmp/mobilenet_v1_1.0_224_quant.tflite",
        help=".tflite model to be executed",
    )
    parser.add_argument(
        "-l",
        "--label_file",
        default="/tmp/labels.txt",
        help="name of file containing labels",
    )
    parser.add_argument("--input_mean", default=127.5, type=float, help="input_mean")
    parser.add_argument(
        "--input_std", default=127.5, type=float, help="input standard deviation"
    )
    parser.add_argument(
        "--num_threads", default=None, type=int, help="number of threads"
    )
    args = parser.parse_args()

    list = os.listdir(args.tests)  
    num_files = len(list)
    print(list)
    print(num_files)
    listOfAllClassifiedImages = []
    for file in list:

        interpreter = tf.lite.Interpreter(
            model_path=args.model_file, num_threads=args.num_threads
        )
        interpreter.allocate_tensors()

        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        # check the type of the input tensor
        floating_model = input_details[0]["dtype"] == np.float32

        # NxHxWxC, H:1, W:2
        height = input_details[0]["shape"][1]
        width = input_details[0]["shape"][2]
        img = Image.open(str(args.tests) + "/" + str(file)).resize((width, height))
        
        # add N dim
        
        input_data = np.expand_dims(img, axis=0)

        if floating_model:
            input_data = (np.float32(input_data) - args.input_mean) / args.input_std

        interpreter.set_tensor(input_details[0]["index"], input_data)

        start_time = time.time()
        interpreter.invoke()
        stop_time = time.time()

        output_data = interpreter.get_tensor(output_details[0]["index"])
        results = np.squeeze(output_data)

        top_k = results.argsort()[-5:][::-1]
        labels = load_labels(args.label_file)
        labelsAndPercentages = {}
        for i in top_k:
            if floating_model:
                labelsAndPercentages[labels[i]] = results[i]
            else:
                print("one of the results of top_k was not a floating_model")
                sys.exit(1)
        

        listOfAllClassifiedImages.append([img,assignLabelToImage(labelsAndPercentages)])
    return listOfAllClassifiedImages

print(classifyImages())