import cv2

img=cv2.imread('Resources/usama.JPG')
cv2.imshow('result',img)
print(img.shape) #image shape

#Resize Image
resize_img=cv2.resize(img,(1000,1000)) #(img,(width,heght))
cv2.imshow('resize_img',resize_img)
print(resize_img.shape)

#Crop Image
crop_img=resize_img[290:1000,160:710] #heigh,width
cv2.imshow('crop_img',crop_img)