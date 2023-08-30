import cv2
from cvzone.HandTrackingModule import HandDetector
import keyboard
import mouse
import threading
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.7, maxHands=2)
ptime = 0

while True:
    success, img = cap.read()

    cTime = time.time()
    fps = 1 / (cTime - ptime)
    ptime = cTime

    cv2.putText(img, f"FPS: {int(fps)}", (40,100), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,255),3)
    hands, img = detector.findHands(img)
    #hands, img = detector.findHands(img)
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1["center"]
        handType1 = hand1["type"]

        fingers1 = detector.fingersUp(hand1)

        if len(hands)==2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            centerPoint2 = hand2["center"]
            handType2 = hand2["type"]

            fingers2 = detector.fingersUp(hand2)
            if fingers1 == [0,1,0,0,0] :
                def Go1():
                    if fingers1 == [0,1,0,0,1]:
                        keyboard.press("w")
                        keyboard.press("space")
                        time.sleep(0.1)
                        keyboard.release("space")
                        keyboard.release("w")
                    else:
                        keyboard.press("w")
                        time.sleep(0.1)
                        keyboard.release("w")
                t1 = threading.Thread(target=Go1)
            if fingers1 == [1,1,0,0,0]:
                keyboard.press("a")
                time.sleep(0.1)
                keyboard.release("a")
            if fingers2 == [1,1,0,0,0]:
                keyboard.press("d")
                time.sleep(0.1)
                keyboard.release("d")
            if fingers2 == [0,0,0,0,1]:
                keyboard.press("S")
                time.sleep(0.1)
                keyboard.release("S")
            if fingers1 == [0,0,0,0,1]:
                keyboard.press("space")
                time.sleep(0.1)
                keyboard.release("space")
            if fingers1 == [1,0,0,0,0] and fingers2 == [1,0,0,0,0]:
                keyboard.press("a")
                keyboard.press("d")
                time.sleep(0.1)
                keyboard.release("a")
                keyboard.release("d")
            if fingers1 == [1,0,0,0,0]:
                mouse.move(-100,0,False,0.1)
            print(fingers1,fingers2)
    #print(len(hands))
    cv2.imshow("Image",img)
    cv2.waitKey(1)