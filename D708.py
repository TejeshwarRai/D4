import cv2
import pytesseract
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

image = cv2.imread("data.PNG", 1)
print(image) # Numpy Array

print("=============")

text = pytesseract.image_to_string(image)
print(text)
