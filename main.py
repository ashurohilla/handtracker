from ast import Try
import cv2
import mediapipe as mp 
import time
import numpy as np
import math
import handtrackingmodule as htm
from time import sleep

import numbersWithFinger
import volumecontrol
import software

def lola():

    # camera gui dimensions
    wCam, hCam = 1700, 900
    pTime = 0
    cTime = 0

    # capturing camera
    cap = cv2.VideoCapture(1)
    cap.set(3, wCam)
    cap.set(4, hCam)

    detector = htm.handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img, draw=True)
        lmList = detector.findPosition(img, draw=False)
        
        # options
        
        if len(lmList) != 0:
            x1, y1 = lmList[8][1], lmList[8][2]
            x2, y2 = lmList[12][1], lmList[12][2]

            # finger tip pointer
            cv2.circle(img, (x1,y1), (15), (30, 144, 255), -1)
            cv2.circle(img, (x2,y2), (15), (30, 144, 255), -1)

        # All options
            # exit
            cv2.rectangle(img, (1680, 50), (1870, 130), (0,0,0), 4, 8)
            cv2.putText(img, str("Exit"), (1720, 100), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0), 3)

            # Counting Fingers
            cv2.rectangle(img, (450, 130), (765, 230), (0, 0, 0), cv2.FILLED)        
            cv2.putText(img, str("Counting Fingers"), (470, 190), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 3)

            # Open Softwares
            cv2.rectangle(img, (800, 130), (1100, 230), (0, 0, 0), cv2.FILLED)        
            cv2.putText(img, str("Open Softwares"), (820, 190), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 3)

            # Control Volume
            cv2.rectangle(img, (1135, 130), (1435, 230), (0, 0, 0), cv2.FILLED)        
            cv2.putText(img, str("Control Volume"), (1155, 190), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 3)

            if (((x1 > 1700 and y1 > 60) and (x1 < 1860 and y1 < 130)) and ((x2 > 1720 and y2 > 80) and (x2 < 1850 and y2 < 130))):
                break
            elif(((x1 > 460 and y1 > 140) and (x1 < 760 and y1 < 220)) and ((x2 > 470 and y2 > 140) and (x2 < 750 and y2 < 210))):
                numbersWithFinger.showNumbers()
            elif(((x1 > 810 and y1 > 140) and (x1 < 1095 and y1 < 220)) and ((x2 > 820 and y2 > 140) and (x2 < 1090 and y2 < 210))):
                software.openSoftwares()
            elif(((x1 > 1150 and y1 > 140) and (x1 < 1400 and y1 < 220)) and ((x2 > 1160 and y2 > 140) and (x2 < 1400 and y2 < 210))):
                volumecontrol.controlVolume()
            

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


lola()