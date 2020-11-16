![VEIL - A Mask Detection Web App](veil.png)

## Index
<ul>
<li><a href="#team">Team</a></li>
<li><a href="#preface">Preface</a></li>
<li><a href="#tools-and-technologies">Tools and Technologies</a></li>
<li><a href="#pre-requisites">Pre-requisites</a></li>
<li><a href="#mission">Mission</a></li>
<li><a href="#current-features">Current Features</a></li>
<li><a href="#watch-our-demo">Watch Our Demo</a></li>
<li><a href="#future-features">Future Features</a></li>
</ul>

## Team
- [Cameron Beaulieu](https://github.com/Cameron-Beaulieu)
- [Evan Kilburn](https://github.com/EvanKilburn)
- [Brandon Ye](https://github.com/yebrandon)
- [Barrett Arbour](https://github.com/barrettarbour)

## Preface 
This project was created as part of the HackHer Hackathon through Queen's University. The design was built as an attempt to create a solution to a modern issue facing society, namely Covid-19

## Tools and Technologies 

### Languages 
- Python 3.8.6
- JavaScript
- CSS
- HTML

### Frameworks
- Flask
- React

### Library
- TensorFlow

### Other
 - [Make Image Classifier](https://github.com/tensorflow/hub/tree/master/tensorflow_hub/tools/make_image_classifier)
 - [Face Recognition 1.3.0](https://pypi.org/project/face-recognition/)
 - Has only been tested for MacOS Terminal

## Pre-requisites
Run The Following Before Running Program 
- pip install "tensorflow~=2.0"
- pip install "tensorflow-hub[make_image_classifier]~=0.6"

## Mission
Veil was developed in hopes of being able to identify those not wearing masks as to create a tool used to help stop the spread of covid. While this was implemented in a web app as a proof of concept, ultimately configuring it to work with real time video capture and integrating it with security cameras would give business a way to identify those not abiding by mask laws. 

## Current Features 
- Image can be captured using laptop camera 
- Image is processed to identify and isolate faces in seperate files
- Faces are processed through machine learning model to determine whether or not the person in the image is wearing a face mask
- The faces are displayed to the screen with an indication of whether or not they are wearing a face mask

## Watch Our Demo
[Demo Video](https://youtu.be/igIYOyoMusU)
## Future Features
 - Train with a larger database to create a more accurate model that can handle more edge cases
 - Change the image capturing to video capture allowing for real time calls to the model 
 - Train the model on improper mask use such as someone not covering their nose 


