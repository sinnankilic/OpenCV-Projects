import cv2
img=cv2.imread("C:/Users/snnklc/Desktop/opencv/haarcascode/3.jpg")

face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

eye=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face.detectMultiScale(gray,1.1,25)

for x,y,w,h in faces:
      cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

      img2=img[y:y+h,x:x+w]
      gray2=gray[y:y+h,x:x+w]

      eyes=eye.detectMultiScale(gray2)
      for x1,y1,w1,h1 in eyes:
            cv2.rectangle(img2,(x1,y1),(x1+w1,y1+h1),(0,255,0),2) 

cv2.imshow("1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
