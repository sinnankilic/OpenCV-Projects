import cv2

cap=cv2.VideoCapture("C:/Users/snnklc/Desktop/opencv/haarcascode/walking.mp4")

body=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")
while True:

      ret, frame=cap.read()

      gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

      bodies=body.detectMultiScale(gray,1.1,5)

      for x,y,w,h in bodies:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

      cv2.imshow("1",frame)
      if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
