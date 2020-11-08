import face_recognition
import numpy as np
import cv2
from PIL import Image, ImageDraw
import time
import keyboard
import os
from pathlib import Path

script_dir= os.getcwd()
script_dir = script_dir+"/tests/"


#open-cv video capabilities
cap = cv2.VideoCapture(0)

def imageProcess():
    removeFiles()
    i = 0
    
    image = face_recognition.load_image_file('screenshot.png')
    face_landmarks_list = face_recognition.face_landmarks(image)    
    face_locations = face_recognition.face_locations(image)

    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()
        pil_image.save(script_dir+'ip'+str(i)+'.jpg')
        i = i + 1

#clears tests folder every time the file is ran
def removeFiles():
    for subdir, dirs, files in os.walk(script_dir):
        for file in files:
            os.remove(script_dir+"/"+file)

removeFiles()
imageProcess()

"""
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    

    if(face_locations != []):
        image = cv2.imwrite('frame.jpg',frame)
        
    cv2.imshow('frame',frame)

    if cv2.waitKey(20) & 0xFF == ord('b'):  # if key 'q' is pressed
        print("kill me")
        imageProcess()

    # Display the resulting frame
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
'''
#reference to the webcam
video_capture = cv2.VideoCapture(0)

while(True):
     ret, frame = video_capture.read()
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break


# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

'''
"""
