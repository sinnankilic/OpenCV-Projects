
import cv2
import matplotlib.pyplot as plt
import numpy as np


image=cv2.imread("a.jpg")

gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


cv2.imshow("gray",gray_scale)
cv2.waitKey(0) 
cv2.destroyAllWindows()
