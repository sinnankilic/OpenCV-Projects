from PIL import Image
import pytesseract

img=Image.open("plate2.jpeg")

text=pytesseract.image_to_string(img,"eng")
print(text)

