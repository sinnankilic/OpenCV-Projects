import cv2

cap=cv2.VideoCapture("trafic.mp4")
car = cv2.CascadeClassifier("C:/Users/snnklc/Desktop/opencv/haarcascode/cars.xml")

while True:
      ret ,frame=cap.read()
      
      gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

      cars=car.detectMultiScale(gray,1.3,2)

      for x,y,w,h in cars:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

      cv2.imshow("a",frame)
      if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cap.release()
cv2.destroyAllWindows()


