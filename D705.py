from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.metrics import r2_score
import cv2
import time

"""
table = pd.read_csv("Advert.csv")
x = table.Radio.values
y = table.Sales.values

print(x.shape)
print(y.shape)

x = x.reshape(len(x),1)     # to convert to 2d
y = y.reshape(len(y),1)

print(x.shape)
print(y.shape)

model = LinearRegression()
model.fit(x, y)             # data should be 2d for fit function

y1 = model.predict(x)
score = r2_score(y, y1)
print(score)

b0 = model.intercept_
b1 = model.coef_
# print(b0, b1)
"""
# cv2
"""
img = cv2.imread("testy.jpg", 1)        # 1 for coloured and zero for b/w

print("Image")
print(img)

print("type")
print(type(img))

print("Shape")
print(img.shape)

print("0th index")
print(img[0])

print("img shape 0th index")
print(img[0].shape)

print("img length 0th index")
print(len(img[0]))

cv2.imshow("title", img)
cv2.waitKey(3000)   # quit after 3 s or when key is pressed
# cv2.waitKey(0)      # no time interval... quit after key is pressed
cv2.destroyAllWindows()
"""
# next
"""
img = cv2.imread("testy.jpg", 1)
resized = cv2.resize(img, (400, 400))

shape =  img.shape
print(shape)
# resized = cv2.resize(img, (shape[0]//2, shape[1]//2))
# cv2.imwrite()             # to save(refer to git)
cv2.imshow("title", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
# next
"""
vid = cv2.VideoCapture(0)

check, frame = vid.read()

print("check")
print(check)

print("frame")
print(frame)

time.sleep(3)

cv2.imshow("vid capture", frame)
cv2.waitKey(0)

vid.release()
cv2.destroyAllWindows()
"""
# next
"""
vid = cv2.VideoCapture(0)

frame = 0

while True:
    frame = frame + 1

    check, frame = vid.read()
    print(frame)
    cv2.imshow("Myvideo", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):     # press q to exit
        break

vid.release()
cv2.destroyAllWindows()
print("total frames captured", frame)
"""