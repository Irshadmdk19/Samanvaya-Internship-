import cv2
import cv2 as cv

img= cv.imread('images/car.jpg')

cv.imshow('Car', img)

cv.waitKey(0)


def rescale(frame, scale=0.65):
    width= int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)
    dimensions = (width, height)
    return  cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resizedImage= rescale(img)
cv.imshow('Resizd image',resizedImage)
cv.waitKey(0)

