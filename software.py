import cv2
import time
import os
import handtrackingmodule as htm
import webbrowser   
import subprocess
 
def showNumbers():
    wCam, hCam = 1700, 900
    
    # cap = cv2.VideoCapture(1)
    cap = cv2.VideoCapture(1)
    cap.set(3, wCam)
    cap.set(4, hCam)
    
    pTime = 0
    
    detector = htm.handDetector(detectionCon=0.75)
    
    tipIds = [4, 8, 12, 16, 20]
    
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
    
        # exit
        cv2.putText(img, str("youtube"), (1720, 100), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0), 3)
        cv2.rectangle(img, (1680, 50), (1870, 130), (0,0,0), 4, 8)

        # Open Softwares
        cv2.putText(img, str("Instagram"), (820, 190), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0), 3)
        cv2.rectangle(img, (800, 130), (1100, 230), (0, 0, 0), 4, 8)        

        # Control Volume
        cv2.putText(img, str("Visual Studio"), (1155, 190), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0), 3)
        cv2.rectangle(img, (1135, 130), (1435, 230), (0, 0, 0), 4, 8)
        if (): 
            subprocess.Popen([dir])
            subprocess.call(dir)
        elif():    
            url = 'https://www.instagram.com/'
            webbrowser.open_new_tab(url)
        elif():    
            url = 'https://www.youtube.com/'
            webbrowser.open_new_tab(url)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
    
        cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 0, 0), 3)
    
        cv2.imshow("Image", img)
        cv2.waitKey(1)