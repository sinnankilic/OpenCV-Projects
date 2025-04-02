
import cv2
import matplotlib.pyplot as plt
import numpy as np


image=cv2.imread("a.jpg")
cv2.imshow("dfds",image)
cv2.waitKey(0) 


gaus=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("gaus",gaus)
cv2.waitKey(0) 


median=cv2.medianBlur(image,5)
cv2.imshow("median",median)
cv2.waitKey(0) 

bileteral=cv2.bilateralFilter(image,9,75,75)
cv2.imshow("bilateral",bileteral)
cv2.waitKey(0)

cv2.destroyAllWindows() 

