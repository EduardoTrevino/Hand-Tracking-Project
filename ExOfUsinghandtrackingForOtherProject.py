import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm


pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while (True):
    success, img = cap.read()
    # can accept mutiple paramaters and remove drawing as to silently detect a finger landmark
    img = detector.findHands(img)
    # can remove drawing under (img, draw=False)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        # returns the specifed landmark as a list indicating landmark number and pixel region detected on camera
        print(lmList[4])

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
