#!/bin/bash

python3 ./faceRecognition.py

python3 test_classifier.py \
  --input_mean 0 --input_std 255 \
  --model_file new_mobile_model.tflite --label_file class_labels.txt \
  --tests tests  
