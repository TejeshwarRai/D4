# OpenCV program to detect face in real time
# import libraries of python OpenCV
# where its functionality resides
import cv2
import numpy as np

# load the required trained XML classifiers
# https://github.com/Itseez/opencv/blob/master/
# data/haarcascades/haarcascade_frontalface_default.xml
# Trained XML classifiers describes some features of some
# object we want to detect a cascade function is trained
# from a lot of positive(faces) and negative(non-faces)
# images.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# https://github.com/Itseez/opencv/blob/master
# /data/haarcascades/haarcascade_eye.xml
# Trained XML file for detecting eyes
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

# capture frames from a camera
cap = cv2.VideoCapture(0)
cv2.namedWindow("img")
goggle=cv2.imread("bg.png")
l=[(0,0),(0,0)]
i=0
eyes=0
# loop runs if capturing has been initialized.
while 1:

	# reads frames from a camera
	ret, img = cap.read()

	# convert to gray scale of each frames
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray=cv2.equalizeHist(gray)

	# Detects faces of different sizes in the input image
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)


	for (x,y,w,h) in faces:
		#To draw a rectangle in a face
		#cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		center = (x + w // 2, y + h // 2)
		#cv2.ellipse(img,center,(w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
		#Detects eyes of different sizes in the input image
		if roi_gray.size!=0:
		    eyes = eye_cascade.detectMultiScale(roi_gray)
		i=0
		#To draw a rectangle in eyes
		for (ex,ey,ew,eh) in eyes:
			#cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
			eye_center = (x + ex + ew // 2, y + ey + eh // 2)
			if i==0:
				l[i]=eye_center
				i=1
			else:
				l[i]=eye_center
				i=0
			radius = int(round((ew + eh) * 0.25))
			cv2.circle(img, eye_center, radius, (0, 0, 0), -1)
			cv2.circle(img, eye_center, radius, (0, 215, 255), 1)
		cv2.line(img,l[0],l[1],(0,0,0),5)

	# Display an image in a window
	cv2.imshow('img',img)

	# Wait for Esc key to stop
	key = cv2.waitKey(1)
	if key == ord('q'):
		break
print(type(eyes))
# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()