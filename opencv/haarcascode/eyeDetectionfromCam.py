import cv2
cap = cv2.VideoCapture(0)


face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

eye=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")


while True:
      ret,frame=cap.read()

      gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

      faces=face.detectMultiScale(gray,1.1,10)

      for x,y,w,h in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

            img2=frame[y:y+h,x:x+w]
            gray2=gray[y:y+h,x:x+w]

            eyes=eye.detectMultiScale(gray2)
            for x1,y1,w1,h1 in eyes:
                  cv2.rectangle(img2,(x1,y1),(x1+w1,y1+h1),(0,255,0),2) 
      cv2.imshow("Face and Eye Detection", frame)
      if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()


