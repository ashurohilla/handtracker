import cv2
import time
import os
import handtrackingmodule as htm
 
def showNumbers():
    wCam, hCam = 1700, 900
    
    # cap = cv2.VideoCapture(1)
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
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
            fingers = []
            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
    
            # 4 Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
    
            # print(fingers)
            totalFingers = fingers.count(1)

            
            # exit
            cv2.putText(img, str("Exit"), (1720, 100), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0), 3)
            cv2.rectangle(img, (1680, 50), (1870, 130), (0,0,0), 4, 8)
            if (((x1 > 1700 and y1 > 60) and (x1 < 1860 and y1 < 130)) and ((x2 > 1720 and y2 > 80) and (x2 < 1850 and y2 < 130))):
                # break
                import main
                main.lola()
            
            
            cv2.rectangle(img, (20, 225), (170, 425), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                        10, (255, 255, 255), 25)

        

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
    
        cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 0, 0), 3)
    
        cv2.imshow("Image", img)
        cv2.waitKey(1)