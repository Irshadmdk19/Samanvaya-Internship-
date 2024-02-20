# This is to play the videos

import time

import cv2 as cv

cap = cv.VideoCapture('output.avi')



while True:
    ret,  frame = cap.read()
    time.sleep(0.5)
    cv.imshow("Web cam", frame)

    if cv.waitKey(1)& 0xFF==ord('x'):
        break
# out.release()

cv.destroyAllWindows()