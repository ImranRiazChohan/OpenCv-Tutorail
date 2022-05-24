import cv2
# read videos
cap=cv2.VideoCapture('Resources/video2.mp4') #read video
while True:  #extract frame
    ret,img=cap.read() #frames and Boolean Value
    cv2.imshow("video",img) #Show the Image
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
