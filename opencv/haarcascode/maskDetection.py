import cv2


cap=cv2.VideoCapture(0)

face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

mouth = cv2.CascadeClassifier("C:/Users/snnklc/Desktop/opencv/haarcascode/haarcascade_mcs_mouth.xml")



while True:
      ret,frame=cap.read()
      frame=cv2.flip(frame,1)
     
      gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

      faces=face.detectMultiScale(gray,1.1,5)

      if len(faces)==0:
            cv2.putText(frame,"yuz tespit edilemedi",(40,40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
      else:
            for x ,y ,w ,h in faces:
                  cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

                  roi = gray[y + int(h/2):y + h, x:x + w]
                  m=mouth.detectMultiScale(roi,1.1,5)
                  
                  if len(m)==0:
                        cv2.putText(frame,"maske var",(40,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

                  else:
                        for x1 ,y1 ,w1 ,h1 in m:
                                
                                    cv2.putText(frame,"maske yok",(40,40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)




      cv2.imshow("a",frame)
      if cv2.waitKey(1)& 0xFF==ord("q"):
            break
cap.release()
cv2.destroyAllWindows()