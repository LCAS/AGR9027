# This script uses the camera mounted on the trilobot to detect and count the number of faces in the image. 
# When the robot is detecting faces, the LEDs are activated in green color, otherwise they are blue.
# This code was taken from https://github.com/kevinmcaleer/companion_bot.git

from picamera2 import Picamera2
import cv2
import numpy
import time
from trilobot import *

# create the robot object
tbot = Trilobot()

# Start the camera once; "RGB888" gives pixels in BGR byte order, which is what OpenCV expects
camera = Picamera2()
camera.configure(camera.create_still_configuration(main={"size": (320, 240), "format": "RGB888"}))
camera.start()

def green_light():
    """Turns all six underlights green (used to show that a face was detected)."""
    # Make the lights green
    tbot.fill_underlighting(0,0,0)
    tbot.set_underlight(LIGHT_FRONT_LEFT, 0,255,0, show=False)
    tbot.set_underlight(LIGHT_MIDDLE_LEFT, 0,255,0, show=False)
    tbot.set_underlight(LIGHT_REAR_LEFT, 0,255,0, show=False)
    tbot.set_underlight(LIGHT_FRONT_RIGHT, 0,255,0, show=False)
    tbot.set_underlight(LIGHT_MIDDLE_RIGHT, 0,255,0, show=False)
    tbot.set_underlight(LIGHT_REAR_RIGHT, 0,255,0, show=False)
    tbot.show_underlighting()

def blue_light():
    """Turns all six underlights blue (used to show that no face was detected)."""
    # Make the lights blue
    tbot.fill_underlighting(0,0,0)
    tbot.set_underlight(LIGHT_FRONT_LEFT, 0,0,255, show=False)
    tbot.set_underlight(LIGHT_MIDDLE_LEFT, 0,0,255, show=False)
    tbot.set_underlight(LIGHT_REAR_LEFT, 0,0,255, show=False)
    tbot.set_underlight(LIGHT_FRONT_RIGHT, 0,0,255, show=False)
    tbot.set_underlight(LIGHT_MIDDLE_RIGHT, 0,0,255, show=False)
    tbot.set_underlight(LIGHT_REAR_RIGHT, 0,0,255, show=False)
    tbot.show_underlighting()

def detect_faces():
    """Captures an image and runs a Haar cascade face detector on it. Lights the
    underlighting green if at least one face is found, blue otherwise. Returns the
    list of detected faces (bounding boxes) and the captured image."""
    #Capture image
    image = camera.capture_array()

    # import the cascade file - needs to be in the same folder
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    print("Found " + str(len(faces)) + " face(s)")
    if len(faces) > 0:
        green_light()
    else:
        blue_light()
    return faces, image
   
while True or KeyboardInterrupt:
    faces, image = detect_faces()
    
