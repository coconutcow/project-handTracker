import cv2
# import time
# import os
import HandTrackingModule as hm

wCam, hCam = 640, 480


# Image capture
# cap = cv2.VideoCapture('jamal.jpg')

# Webcam capture
cap = cv2.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)
currentTime=0
startTime=0
detect=hm.handDetector()
totalFingers=0
fingerID=[4,8,12,16,20]

while True:
    success, img = cap.read()
    img = detect.findHands(img)

    lmList = detect.findPosition(img,draw=False)

    print(lmList)


    if len(lmList)!=0:
        fingers=[]

        #Thumb
        if lmList[fingerID[0]][1] > lmList[fingerID[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Four Fingers
        for id in range(1, 5):
            if lmList[fingerID[id]][2] < lmList[fingerID[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        # print(fingers)

        totalFingers=fingers.count(1)
        cv2.rectangle(img, (0, 0), (90, 90), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (25, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
        print(totalFingers)

    #FPS
    # currentTime = time.time()
    # fps = 1/(currentTime-startTime)
    # startTime = currentTime
    # cv2.putText(img,str(int(fps)),(200,70),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,0),2)

    img = cv2.resize(img, (1280, 960))
    cv2.imshow("Image", img)
    cv2.waitKey(1)