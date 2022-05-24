import cv2

# Read Images video Webcam
#   read Image
img=cv2.imread("Resources/usama.JPG") #read image
cv2.imshow("Output",img) #show the image
cv2.waitKey(0)  #output occurs on screen