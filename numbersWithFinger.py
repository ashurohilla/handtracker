import cv2
import time
import os
import handtrackingmodule as htm
 
def showNumbers():
    wCam, hCam = 1700, 900
    
    # cap = cv2.VideoCapture(1)
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    
    pTime = 0
    
    detector = htm.handDetector(detectionCon=0.75)
    
    tipIds = [4, 8, 12, 16, 20]
    
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
    
        cv2.putText(img, str("Exit"), (1650, 100), cv2.FONT_HERSHEY_PLAIN, 4, (0,0,0), 3)
        cv2.rectangle(img, (1630, 50), (1800, 110), (0,0,0), 4, 8)
        
        if len(lmList) != 0:
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]
            p1, z1 = lmList[20][1], lmList[20][2] 
            p2, z2 = lmList[4][1], lmList[4][2]
            fingers = []
            if ((x1 >= 1620 and y1 >= 190) and (x1 <= 1820 and y1 <= 400)):
                print("cola")
                break
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
            # print(totalFingers)
    
            # h, w, c = overlayList[totalFingers - 1].shape
            # img[0:h, 0:w] = overlayList[totalFingers - 1]
    
            cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                        10, (255, 0, 0), 25)

        

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
    
        cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 0, 0), 3)
    
        cv2.imshow("Image", img)
        cv2.waitKey(1)