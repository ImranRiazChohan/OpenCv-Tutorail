import cv2
import numpy as np
img=cv2.imread("Resources/00090.jpg")
kernel=np.ones((5,5),np.uint8)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Convert into gray Image
img_blur=cv2.GaussianBlur(img_gray,(7,7),0) #Blur Image
img_Canny=cv2.Canny(img_gray,100,170) #Edge Detection
img_dialation=cv2.dilate(img_Canny,kernel,iterations=2)
img_enrode=cv2.erode(img_dialation,kernel,iterations=2)
cv2.imshow('Orignal Image',img)
cv2.imshow('gray Image',img_gray)
cv2.imshow('Blur Image',img_blur)
cv2.imshow('Canny Image',img_Canny)
cv2.imshow('Dialation Image',img_dialation)
cv2.imshow('Enrode Image',img_enrode)
cv2.waitKey(0)