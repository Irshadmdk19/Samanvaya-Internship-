import cv2
import numpy as np
img= cv2.imread('fruits.jpg')

cv2.imshow('Original Imgae',img)

#Playing with RGB
imgBlue=img[:,:,0]
imgGreen=img[:,:,1]
imgRed=img[:,:,2]
new_img=np.hstack((imgBlue,imgGreen,imgRed))

#Resize
img_resize=cv2.resize(img,(200,200))
img_resize_by_percentage=cv2.resize(img,(img.shape[0]//3,img.shape[1]//3)) #30%

#Flip
img_flip_vertical=cv2.flip(img,0)
img_flip_horizontal=cv2.flip(img,1)
img_flip_both=cv2.flip(img,-1)

#Cropping
img_crop=img[0:300,0:100]

#Saving Image
cv2.imwrite('Crop_fruits.png',img_crop)

#Drawing Shapes
img_bg=np.zeros((512,512,3))

cv2.rectangle(img_bg, pt1=(100,100),pt2=(400,400),color=(255,0,0),thickness=3)
cv2.circle(img_bg,center=(100,400),radius=50,color=(0,255,0),thickness=3)
cv2.line(img_bg,pt1=(200,200),pt2=(300,450),color=(0,0,255),thickness=3)
cv2.putText(img_bg,org=(100,100),fontScale=2,color=(0,255,255),thickness=2,lineType=cv2.LINE_AA,text="hello",fontFace=cv2.FONT_HERSHEY_PLAIN)

#OPEN_CV Events

def draw(event,x,y,flags,params):
    if event==1:
        cv2.circle(img_new,center=(x,y),radius=20,color=(255,255,0),thickness=-1)

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)

img_new=np.zeros((512,512,3))
while True:

    cv2.imshow("window",img_new)

    if cv2.waitKey(1) & 0xFF==ord('x'):
        break

cv2.destroyAllWindows()

#Display
cv2.imshow("Fruits",img)
cv2.waitKey(0)



