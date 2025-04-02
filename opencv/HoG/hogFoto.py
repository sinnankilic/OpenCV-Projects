import cv2
from skimage.feature import hog
from skimage import exposure


img = cv2.imread("C:/Users/snnklc/Desktop/opencv/HoG/atam.jpeg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

x, hogimg=hog(gray,visualize=True)
rescaled=exposure.rescale_intensity(hogimg,in_range=(0,10))
cv2.imshow("hog",hogimg)
cv2.imshow("orj",img)
cv2.imshow("fd",rescaled)

cv2.waitKey(0)
cv2.destroyAllWindows()
