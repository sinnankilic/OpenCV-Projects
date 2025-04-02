import cv2

import pickle
liste=[]

try:
      with open("konum","rb") as f:
            liste=pickle.load(f)
except:
      liste=[]

def mouse(events,x,y,flags,params):

      if events==cv2.EVENT_LBUTTONDOWN:
            liste.append((x,y))

      if events == cv2.EVENT_RBUTTONDOWN:
            for i,pos in enumerate(liste):
                  x1,y1=pos
                  if x1<x<x1+26 and y1<y<y1+15:
                        liste.pop(i)
      with open ("konum","wb") as f:
            pickle.dump(liste,f)




while True:
      img = cv2.imread("C:/Users/snnklc/Desktop/opencv/otopark/first_frame.png")
      print(liste)
      for l in liste:
            cv2.rectangle(img, l, (l[0]+26, l[1]+15), (255, 0, 0), 2)


      cv2.imshow("img",img)
      cv2.setMouseCallback("img",mouse)
      if cv2.waitKey(1)& 0xff ==ord("q"):
            break


cv2.destroyAllWindows()
