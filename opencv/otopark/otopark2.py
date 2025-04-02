import cv2

import pickle
import numpy as np

cap=cv2.VideoCapture("C:/Users/snnklc/Desktop/opencv/otopark/video.mp4")



# def func(frame1):
#       counter=0
#       for pos in liste:
#             x,y=pos
#             crop=frame1[y:y+15,x:x+26]

#             counter=cv2.countNonZero(crop)

#             if counter<150:
#                   color=(0,255,0)
#             else:
#                   color=(0,0,255)
#             cv2.rectangle(frame1, pos, (pos[0]+26, pos[1]+15), color, 2)


def func(mask, frame_draw):
      counter = 0
      for pos in liste:
        x, y = pos
        crop = mask[y:y+15, x:x+26]

        count = cv2.countNonZero(crop)

        if count < 150:
            color = (0, 255, 0)  # yeşil: boş
            counter+=1
        else:
            color = (0, 0, 255)  # kırmızı: dolu

        cv2.rectangle(frame_draw, (x, y), (x+26, y+15), color, 2)

      cv2.putText(frame,f"bos: {counter}/{len(liste)}",(15,24),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),3)


with open("konum","rb") as f:
      liste=pickle.load(f)
while True:
      ret, frame=cap.read()
      gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

      blur=cv2.GaussianBlur(gray,(3,3),1)
      thresh=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)

      median=cv2.medianBlur(thresh,5)
      dilates = cv2.dilate(median, np.ones((3, 3), np.uint8), iterations=1)

      func(dilates,frame)
      cv2.imshow("frame",frame)
      # cv2.imshow("thresh",thresh)
      # cv2.imshow("blur",blur)
      # cv2.imshow("median",median) 
      # cv2.imshow("bilates",dilates)



      if cv2.waitKey(200)& 0xff==ord("q"):
            break

cap.release()
cv2.destroyAllWindows()