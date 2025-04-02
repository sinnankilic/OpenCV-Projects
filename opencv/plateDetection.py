import cv2
import numpy as np
import pytesseract
import imutils
import dlib


img=cv2.imread("plate2.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

filter = cv2.GaussianBlur(gray, (5, 5), 0)

corner = cv2.Canny(filter, 30, 150)



contour,a=cv2.findContours(corner,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt=imutils.grab_contours((contour,a))
cnt=sorted(cnt,key=cv2.contourArea,reverse=True)[:10]

ekran = None

for i in cnt:
      eps=0.018*cv2.arcLength(i,True)
      aprx=cv2.approxPolyDP(i,eps,True)
      if len(aprx)==4:
            ekran=aprx
            break

mask=np.zeros(gray.shape,np.uint8)
newmask=cv2.drawContours(mask,[ekran],0,(255,255,255),-1)
text=cv2.bitwise_and(img,img,mask=mask)
(x,y)=np.where(mask==255)
(x1,y1)=(np.min(x),np.min(y))
(x2,y2)=(np.max(x),np.max(y))
kirp=gray[x1:x2+1,y1:y2+1]




result=pytesseract.image_to_string(kirp,lang="eng")
print(result)

cv2.waitKey(0)
cv2.destroyAllWindows()

