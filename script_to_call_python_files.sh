#!/bin/bash

python ./faceRecognition.py

python ./label_image.py \
  --input_mean 0 --input_std 255 \
  --model_file new_mobile_model.tflite --label_file class_labels.txt \
  --image tests/NoMask3.jpg