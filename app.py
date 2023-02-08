import cv2
import pyautogui
from cvzone.HandTrackingModule import HandDetector

hand_detector = HandDetector(detectionCon=0.8, maxHands=2)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hands, img = hand_detector.findHands(frame)
    if hands:
        lmlist = hands[0]
        fingerUp = hand_detector.fingersUp(lmlist)
        # print(fingerUp) # buat nyari tau jumlah jari yang diangkat

        # styling

        # color : (B,G,R)
        blue = (255,0,0)
        green = (0,200,0)
        red = (0,0,255)
        yellow = (0,255,200)

        font = cv2.FONT_HERSHEY_DUPLEX
        position = (30,80)

        # clench // kepal
        if fingerUp == [0, 0, 0, 0, 0]:
            cv2.putText(frame, "Neutral", position, font, 1, yellow, 1, cv2.LINE_AA)
            pyautogui.press('s')

        # pointing ahead // nunjuk ke depan
        elif fingerUp == [1,1,0,0,0]:
            cv2.putText(frame, "Forward", position, font, 1, blue, 1, cv2.LINE_AA)
            pyautogui.press('up')

        # pointing backward (with thumb) // nunjuk ke belakang (pake jempol)
        elif fingerUp == [1,0,0,0,0]:
            cv2.putText(frame, "Backward", position, font, 1, blue, 1, cv2.LINE_AA)
            pyautogui.press('down')

        # index up // telunjuk ke atas
        elif fingerUp == [0, 1, 0, 0, 0]:
            cv2.putText(frame, "Reduce throttle ", position, font, 1, green, 1, cv2.LINE_AA)
            pyautogui.press('a')

        # index with middle // telunjuk dengan jari tengah
        elif fingerUp == [0, 1, 1, 0, 0]:
            cv2.putText(frame, "Increase throttle", position, font, 1, green, 1, cv2.LINE_AA)
            pyautogui.press('z')

        # index, middle, and ring // telunjuk, jari tengah, dan jari manis
        elif fingerUp == [0, 1, 1, 1, 0]:
            cv2.putText(frame, "Reduce Brake", position, font, 1, red, 1, cv2.LINE_AA)
            pyautogui.press(',')

        # index, middle, ring, and little // telunjuk, jari tengah, jari manis, dan kelingking
        elif fingerUp == [0, 1, 1, 1, 1]:
            cv2.putText(frame, "Increase Brake", position, font, 1, red, 1, cv2.LINE_AA)
            pyautogui.press('.')

        # all finger (5 figer) // semua jari (5 jari)
        elif fingerUp == [1, 1, 1, 1, 1]:
            cv2.putText(frame, "Emergency Brake", position, font, 1, red, 1, cv2.LINE_AA)
            pyautogui.press('/')

        # "ok" 
        elif fingerUp == [1,0,1,1,1]:
            cv2.putText(frame, "Horn", position, font, 1, red, 1, cv2.LINE_AA)
            pyautogui.press('enter')
            
    cv2.imshow("BVE-Pressless", frame)
    k = cv2.waitKey(1)

    # close with "X" button // menutup pake tombol "X"
    if cv2.getWindowProperty('BVE-Pressless',cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows() 