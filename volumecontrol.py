
import cv2
import time
import numpy as np
import volumecontrolmodule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
################################

def controlVolume():
    wCam, hCam = 1700, 900
    cap = cv2.VideoCapture(1)
    # cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    pTime = 0
    
    detector = htm.handDetector( detectionCon=0.75)
    
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # volume.GetMute()
    # volume.GetMasterVolumeLevel()
    volRange = volume.GetVolumeRange()
    minVol = volRange[0]
    maxVol = volRange[1]
    vol = 0
    volBar = 400
    volPer = 0
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)   
        
        if len(lmList) != 0:
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[12][1], lmList[12][2]
            
            x3, y3 = lmList[8][1], lmList[8][2]

            cx, cy = (x1 + x3) // 2, (y1 + y3) // 2
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x3, y3), (255, 0, 255), 3)
            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            length = math.hypot(x3 - x1, y3 - y1)
            

            vol = np.interp(length, [50, 300], [minVol, maxVol])
            volBar = np.interp(length, [50, 300], [400, 150])
            volPer = np.interp(length, [50, 300], [0, 100])
            # print(int(length), vol)
            volume.SetMasterVolumeLevel(vol, None)

             # exit
            cv2.putText(img, str("Exit"), (1720, 100), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0), 3)
            cv2.rectangle(img, (1680, 50), (1870, 130), (0,0,0), 4, 8)
            if (((x2 > 1700 and y2 > 60) and (x2 < 1860 and y2 < 130)) and ((x3 > 1720 and y3 > 80) and (x3 < 1850 and y3 < 130))):
                break
                
            if length < 50:
                cv2.circle(img, (cx, cy), 15, (0, 0, 0), cv2.FILLED)
                
        cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 0), 3)
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                    1, (0, 0, 0), 3)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                    1, (0, 0, 0), 3)
        cv2.imshow("Img", img)
        cv2.waitKey(1)