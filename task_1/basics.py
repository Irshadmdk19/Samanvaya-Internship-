import cv2
import cv2 as cv

img = cv.imread('images/car.jpg')
cv.imshow('Car',img)
cv2.waitKey(0)

#Grayscale image

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("gray",gray)
cv2.waitKey(0)

#Blurring the image
blur=cv.GaussianBlur(img,(9,9), cv.BORDER_DEFAULT)
cv.imshow('Blurred image',blur)
cv2.waitKey(0)

#Edge cascade (Canny edge detection)
canny = cv.Canny(img,125,175)
cv.imshow("Caan image", canny)
cv2.waitKey(0)

#Dilating the image
dilated =cv.dilate(canny,(9,9), iterations=3)
cv.imshow("Dilated img", dilated)
cv2.waitKey(0)

#Eroding
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow("Erored img", eroded )
cv2.waitKey(0)

#Resizing
resized = cv.resize(img,(200,600), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized img",resized)
cv2.waitKey(0)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped img", cropped)
cv2.waitKey(0)