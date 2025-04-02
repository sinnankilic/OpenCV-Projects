import cv2
import numpy as np 

cap = cv2.VideoCapture("LaneDetection.mp4")

while True:
      a, frame = cap.read()

      if not a:  # video bittiğinde çık
            break

      frame = cv2.resize(frame, (800, 600))
      hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

      # Renk aralığı: sarımsı renkler için örnek
      low = np.array([0, 0, 220], dtype=np.uint8)
      high = np.array([180, 20, 255], dtype=np.uint8)

      # Maskeyi oluştur
      mask = cv2.inRange(hsv, low, high)
      kenar=cv2.Canny(mask,75,250)
      cizgi=cv2.HoughLinesP(kenar,1,np.pi/180,50,maxLineGap=5)


      for i in cizgi:
            x1,y1,x2,y2=i[0]
            cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)

      cv2.imshow("video", frame)
      fps = cap.get(cv2.CAP_PROP_FPS)
      delay = int(1000 / fps)


      # q'ya basınca çık
      if cv2.waitKey(2) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
