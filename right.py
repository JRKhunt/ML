import cv2
img=cv2.imread("4.jpg",cv2.IMREAD_COLOR)
face_cascade=cv2.CascadeClassifier("haarcascade_mcs_rightear.xml")
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(grey_img,1.1,3)
print(faces)
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow("rightear Detector",img)
cv2.waitKey(5000)
cv2.destroyAllWindows()