
import cv2 as cv

img = cv.imread('mul_faces.jpg')
cv.imshow('Group of people',img)
cv.waitKey(0)

grayscale=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale',grayscale)
cv.waitKey(0)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(grayscale,scaleFactor=1.1, minNeighbors=9)

# Harcascade are not suitable for more advanced cv projects as it is more prone to noice
print(f'No of faces founf = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow('Detected Faces', img)
cv.waitKey(0)