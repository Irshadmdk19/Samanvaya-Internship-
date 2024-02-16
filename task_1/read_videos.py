import cv2 as cv

capture = cv.VideoCapture('videos/sample.mp4')

while True:
    isTrue, frame= capture.read();
    cv.imshow('Video', frame)

    if cv.waitKey(10) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()