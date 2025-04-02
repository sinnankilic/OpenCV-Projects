import cv2

img=cv2.imread("C:/Users/snnklc/Desktop/opencv/haarcascode/ismailhocam.jpeg")

body=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

img=cv2.resize(img,(600,600))

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

bodies=body.detectMultiScale(gray,1.1,2)

for x,y,w,h in bodies:
      cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("1",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
