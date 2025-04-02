import cv2
import matplotlib.pyplot as plt
import numpy as np


image=plt.imread("a.jpg")

gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
histg = cv2.calcHist([gray_scale],[0],None,[256],[0,256]) 



plt.plot(histg)
plt.show()
cv2.waitKey(0) 
cv2.destroyAllWindows()