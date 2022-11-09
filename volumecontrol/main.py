from ast import Try
import cv2
import mediapipe as mp 
import time
import numpy as np
import math
import volumecontrolmodule as htm
#from cvzone.SerialModule import SerialObject
from time import sleep
import serial
try:
    arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
except:
    print("port not found")    
#arduino = SerialObject("COM11")
wCam, hCam = 1240,780
pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector()
def write_read(leng,lent):
    length = int(leng)
    fingerlength = int(lent)
    arduino.write([length])
    data = arduino.readline()
    return data
while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        p1, z1 = lmList[20][1], lmList[20][2]
        p2, z2 = lmList[4][1], lmList[4][2]
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.line(img, (p1, z1), (p2, z2), (255, 0, 255), 3)
        length = math.hypot(x2 - x1, y2 - y1)
        lengthp = math.hypot(p1 - p2, z1 - z2)
        vol = np.interp(length, [15, 600], [0, 100])
        vol2 =np.interp(lengthp, [15, 600], [0, 100])
        #print(vol)
        #value = write_read(vol, vol2)
        #print(value)
        #arduino.sendData([leng])


        
        #print(lmList[4], length)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
     #           (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)