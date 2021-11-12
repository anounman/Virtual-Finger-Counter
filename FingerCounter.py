import model.hand as hand
import mediapipe as mp
import cv2
import time
import numpy as np


width = 1280
height = 720

camera = cv2.VideoCapture(1)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
detection = hand.HandDetection()
while True:
    fingersCount = 0
    success , img = camera.read()
    img = cv2.flip(img, 1)
    img = detection.findHand(img)
    landmarks = detection.findPosition(img)
    if len(landmarks) != 0:
        fingers = detection.fingersUp()
        if len(fingers) != 0:
            if fingers[0]:
                fingersCount += 1
                cv2.putText(img, "Finger: " + "Thumb", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 , 255), 2)
    
            if fingers[1]:
                fingersCount += 1
                cv2.putText(img, "Finger: " + "Index", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 , 255), 2)
            if fingers[2]:
                fingersCount += 1
                cv2.putText(img, "Finger: " + "Middle", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 , 255), 2)
            if fingers[3]:
                fingersCount += 1
                cv2.putText(img, "Finger: " + "Ring", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 , 255), 2)
            if fingers[4]:
                fingersCount += 1
                cv2.putText(img, "Finger: " + "Pinky", (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 , 255), 2)
            if fingers[2] and fingersCount == 1 :
                cv2.putText(img, "FUCK YOU", (160, 210), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 , 255), 2)
           
    cv2.putText(img, "Fingers: " + str(fingersCount), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 , 255), 2)
    cv2.imshow('img',img)
    cv2.waitKey(1)