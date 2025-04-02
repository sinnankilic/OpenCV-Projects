


import cv2 as cv
import face_recognition
import dlib

detector=dlib.get_frontal_face_detector()

# Referans yüz yükle
sinan_image = face_recognition.load_image_file("C:/Users/snnklc/Desktop/opencv/faceRecognize/SinanKILIÇ.jpg")
sinan_encoding = face_recognition.face_encodings(sinan_image, num_jitters=50, model='large')[0]

# Kamerayı başlat
cam = cv.VideoCapture(0)

if not cam.isOpened():
    print("Camera not working")
    exit()

while True:
    ret, frame = cam.read()
    if not ret:
        print("Can't receive the frame")
        break

    # Yüzleri bul
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations, num_jitters=10, model='large')

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        match = face_recognition.compare_faces([sinan_encoding], face_encoding)[0]

        # Dikdörtgen çiz
        cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        if match:
            name = "Sinan KILIÇ"
            print(f'{name} bulundu!')
        else:
            name = "Bilinmeyen"

        # İsim yazdır
        cv.putText(frame, name, (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    # Kamerayı göster
    cv.imshow("Face Recognition", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Temizlik
cam.release()
cv.destroyAllWindows()
