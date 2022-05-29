import numpy as np
import cv2


img=cv2.imread('Resources/cards.jfif')

height,width=350,250
pts1=np.float32([[495,27],[576,204],[244,146],[323,320]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)
output=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow('img',img)

cv2.imshow('output',output)

cv2.imwrite('Resources/king.jpg',output)
cv2.waitKey(0)