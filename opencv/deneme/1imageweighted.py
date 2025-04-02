import cv2
import matplotlib.pyplot as plt
import numpy as np



image = cv2.imread("a.jpg")
image2 = cv2.imread("araba.jpg")

if image.shape != image2.shape:
    image2 = cv2.resize(image2, (image.shape[1], image.shape[0]))


weight = cv2.addWeighted(image, 0.5, image2, 0.6, 0)

# Sonucu göster
cv2.imshow("Weighted Image", weight)
cv2.waitKey(0)
cv2.destroyAllWindows()
