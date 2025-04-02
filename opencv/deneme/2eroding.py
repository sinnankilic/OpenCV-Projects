import cv2
import matplotlib.pyplot as plt
import numpy as np


image=cv2.imread("araba.jpg")

h, w=image.shape[:2]
new_wid=1200

new_heig=int(new_wid*(h/w))

re=cv2.resize(image,(new_wid,new_heig))

kernel=np.ones((6,6),np.int8)
img=cv2.erode(re,kernel,cv2.BORDER_REFLECT)
cv2.imshow("araba",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

