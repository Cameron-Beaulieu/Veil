from PIL import Image, ImageDraw
import face_recognition
import os
script_dir = os.path.dirname(__file__)
script_dir = script_dir+"/processedImages/"

#basic image processing. If it returns an empty array than person is wearing mask or is not a person and shouldn't be flagged
# Load the jpg file into a numpy array
picList = ["barrett.jpg", "test.jpg", "mask.jpg"]
i = 0;
while i <  len(picList):
    #load image
    image = face_recognition.load_image_file(picList[i])
    # Find all facial features in all the faces in the image
    face_landmarks_list = face_recognition.face_landmarks(image)
    #face has been detected
    if(len(face_landmarks_list)!=0):
        face_locations = face_recognition.face_locations(image)
        for face_location in face_locations:
            # Print the location of each face in this image
            top, right, bottom, left = face_location
            # You can access the actual face itself like this:
            face_image = image[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            pil_image.show()
            pil_image.save(script_dir+picList[i])
    i=i+1
    



