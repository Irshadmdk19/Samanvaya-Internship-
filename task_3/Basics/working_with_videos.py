import cv2 as cv

cap = cv.VideoCapture(0)
fourcc= cv.VideoWriter_fourcc(*'XVID')
out=cv.VideoWriter('output.avi', fourcc,20.0,(640,480))


while True:
    ret,  frame = cap.read()

    cv.imshow("Web cam", frame)

    if cv.waitKey(1)& 0xFF==ord('x'):
        break
out.release()
cv.destroyAllWindows()