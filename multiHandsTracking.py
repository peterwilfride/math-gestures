from cv2 import cv2
from cvzone.HandTrackingModule import HandDetector
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

pTime = 0

def handState_left(lmHand):
    # all the fingers start open
    # thumb, index, middle, ring, pinky
    hand_state = [1, 1, 1, 1, 1]

    if lmHand[4][0] > lmHand[3][0]:
        hand_state[0] = 0
    if lmHand[8][1] > lmHand[6][1]:
        hand_state[1] = 0
    if lmHand[12][1] > lmHand[10][1]:
        hand_state[2] = 0
    if lmHand[16][1] > lmHand[14][1]:
        hand_state[3] = 0
    if lmHand[20][1] > lmHand[18][1]:
        hand_state[4] = 0
    
    return hand_state

def handState_right(lmHand):
    # all the fingers start open
    # thumb, index, middle, ring, pinky
    hand_state = [1, 1, 1, 1, 1]

    if lmHand[4][0] < lmHand[3][0]:
        hand_state[0] = 0
    if lmHand[8][1] > lmHand[6][1]:
        hand_state[1] = 0
    if lmHand[12][1] > lmHand[10][1]:
        hand_state[2] = 0
    if lmHand[16][1] > lmHand[14][1]:
        hand_state[3] = 0
    if lmHand[20][1] > lmHand[18][1]:
        hand_state[4] = 0
    
    return hand_state

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        if len(hands) == 2:
            hand1, hand2 = hands

            lmList1 = hand1["lmList"]
            lmList2 = hand2["lmList"]
            
            #handtype1 = hand1["type"]
            #handtype2 = hand2["type"]

            value1 = sum(handState_left(lmList1))
            value2 = sum(handState_right(lmList2))

            print(value1, value2)

            cv2.putText(img, f'{value1+value2}', (300,430), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 0, 0), 2)
        else:
            cv2.putText(img, "Put your 2 hands", (200,30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)
    else:
        cv2.putText(img, "Put your hands", (200,30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (520,30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)       

    cv2.imshow("Img", img)
    cv2.waitKey(1)