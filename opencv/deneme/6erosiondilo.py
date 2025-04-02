
import cv2
import matplotlib.pyplot as plt
import numpy as np


image=cv2.imread("a.jpg")

gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
kernel = np.ones((5, 5), np.uint8) 

image_ero=cv2.erode(gray_scale,kernel,iterations=2)
image_dilo=cv2.dilate(gray_scale,kernel,iterations=2)

cv2.imshow('Input', gray_scale) 
cv2.imshow('Erosion', image_ero) 
cv2.imshow('Dilation',image_dilo) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
