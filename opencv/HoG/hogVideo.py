import cv2
from skimage.feature import hog
from skimage import exposure


cap=cv2.VideoCapture(0)

while True:
      ret,frame=cap.read()
      gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

      x, hogImg=hog(gray,visualize=True)
      rescale=exposure.rescale_intensity(hogImg,in_range=(0,10))
      cv2.imshow("hog",rescale)
      if cv2.waitKey(5)& 0xff==ord("q"):
            break
     

cv2.waitKey(0)
cv2.destroyAllWindows()
