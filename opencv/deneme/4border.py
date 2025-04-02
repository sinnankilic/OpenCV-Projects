
import cv2
import matplotlib.pyplot as plt
import numpy as np


image=cv2.imread("a.jpg")
image=cv2.copyMakeBorder(image,15,15,15,15,cv2.BORDER_CONSTANT)
cv2.imshow("border",image)
cv2.waitKey(0) 
