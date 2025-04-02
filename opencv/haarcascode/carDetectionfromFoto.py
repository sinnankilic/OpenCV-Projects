import cv2

img=cv2.imread("C:/Users/snnklc/Desktop/opencv/haarcascode/car1.jpg")


car = cv2.CascadeClassifier("C:/Users/snnklc/Desktop/opencv/haarcascode/cars.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cars=car.detectMultiScale(gray,1.02,4)

for x,y,w,h in cars:
      cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("a",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


