import cv2
import time
import os
import handtrackingmodule as htm
import webbrowser   
import subprocess
 
def openSoftwares():
    wCam, hCam = 1700, 900
    
    # cap = cv2.VideoCapture(0)
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
        if len(lmList) != 0:
            x1, y1 = lmList[8][1], lmList[8][2]
            x2, y2 = lmList[12][1], lmList[12][2]
            # exit
            cv2.putText(img, str("Exit"), (1720, 100), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0), 3)
            cv2.rectangle(img, (1680, 50), (1870, 130), (0,0,0), 4, 8)
            if (((x1 > 1700 and y1 > 60) and (x1 < 1860 and y1 < 130)) and ((x2 > 1720 and y2 > 80) and (x2 < 1850 and y2 < 130))):
                import main
                main.lola()
            
            # Counting Fingers
            cv2.rectangle(img, (450, 390), (765, 490), (0, 0, 0), cv2.FILLED)        
            cv2.putText(img, str("Youtube"), (470, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255), 4)

            # Open Softwares
            cv2.rectangle(img, (800, 390), (1100, 490), (0, 0, 0), cv2.FILLED)        
            cv2.putText(img, str("Spotify"), (820, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255), 4)

            # Control Volume
            cv2.rectangle(img, (1135, 390), (1435, 490), (0, 0, 0), cv2.FILLED) 
            cv2.putText(img, str("Instagram"), (1155, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255), 4)

            if (((x1 > 460 and y1 > 408) and (x1 < 760 and y1 < 480)) and ((x2 > 470 and y2 > 408) and (x2 < 750 and y2 < 470))): 
                url = 'https://www.youtube.com/'
                webbrowser.open_new_tab(url)
                time.sleep(2)
            elif(((x1 > 810 and y1 > 408) and (x1 < 1095 and y1 < 480)) and ((x2 > 820 and y2 > 408) and (x2 < 1090 and y2 < 470))):    
                dir = 'C:/Users/right/AppData/Roaming/Spotify/Spotify.exe'
                subprocess.Popen([dir])
                subprocess.call(dir)
            elif(((x1 > 1150 and y1 > 408) and (x1 < 1400 and y1 < 480)) and ((x2 > 1160 and y2 > 408) and (x2 < 1400 and y2 < 470))):    
                url = 'https://www.instagram.com/'
                webbrowser.open_new_tab(url)
                time.sleep(2)
            
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
    
        cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 0, 0), 3)
    
        cv2.imshow("Image", img)
        cv2.waitKey(1)