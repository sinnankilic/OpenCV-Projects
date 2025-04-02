import cv2

img = cv2.imread("C:/Users/snnklc/Desktop/opencv/haarcascode/3.jpg")

if img is None:
    print("HATA: Görüntü dosyası yüklenemedi. Dosya yolu veya adı hatalı.")
    exit()

face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

if face.empty():
    print("HATA: Haarcascade XML dosyası yüklenemedi.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face.detectMultiScale(gray, 1.1, 4)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Göster
cv2.imshow("Detected Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
