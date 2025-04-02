import cv2
import matplotlib.pyplot as plt
import numpy as np


image=plt.imread("a.jpg")

gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

x,thresh=cv2.threshold(gray_scale,120,255,cv2.THRESH_BINARY)
ret, thresh1 = cv2.threshold(gray_scale, 120, 255, cv2.THRESH_BINARY + 
                                            cv2.THRESH_OTSU)      

cv2.imshow('Binary Threshold', thresh) 
cv2.imshow('Binary Threshold1', thresh1) 



cv2.waitKey(0) 
cv2.destroyAllWindows()