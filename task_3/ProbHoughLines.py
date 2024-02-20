import cv2
import cv2 as cv
import numpy as np
img=cv.imread('images/sudoku_2.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale",gray)
edges=cv.Canny(gray,50,150, apertureSize=3)
cv.imshow('Edges',edges)

lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)

for line in lines:
    x1,y1,x2,y2=line[0]
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)


cv2.imshow("Output image",img)
cv.waitKey(0);
# cv.destroyAllWindows()
