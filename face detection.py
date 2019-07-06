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
		cv2.line(img,l[0],l[1],(0,0,0),2)

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

# ==================================================================== #

# from __future__ import print_function
# import cv2 as cv
# import argparse
#
# def detectAndDisplay(frame):
#     frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     frame_gray = cv.equalizeHist(frame_gray)
#
#     #-- Detect faces
#     faces = face_cascade.detectMultiScale(frame_gray)
#     for (x,y,w,h) in faces:
#         center = (x + w//2, y + h//2)
#         # frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
#
#         faceROI = frame_gray[y:y+h,x:x+w]
#         #-- In each face, detect eyes
#         i = 0
#         l=[(0,0),(0,0)]
#         eyes = eyes_cascade.detectMultiScale(faceROI)
#         for (x2,y2,w2,h2) in eyes:
#             eye_center = (x + x2 + w2//2, y + y2 + h2//2)
#             if i==0:
#                 # l.append(eye_center)
#                 l[0]=eye_center
#                 i=1
#             else:
#                 # l.append(eye_center)
#                 l[1]= eye_center
#                 i=0
#             radius = int(round((w2 + h2)*0.25))
#             frame = cv.circle(frame, eye_center, radius, (255, 192, 69 ), -2, 4)
#             frame = cv.circle(frame, eye_center, radius, (255, 0, 0),5, 4)
#         frame = cv.line(frame, l[0], l[1], (255, 0, 0), 5)
#
#     cv.imshow('Capture - Face detection', frame)
#
# parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
# parser.add_argument('--face_cascade', help='Path to face cascade.', default='haarcascade_frontalface_alt.xml')
# parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='haarcascade_eye_tree_eyeglasses.xml')
# parser.add_argument('--camera', help='Camera devide number.', type=int, default=0)
# args = parser.parse_args()
#
# face_cascade_name = args.face_cascade
# eyes_cascade_name = args.eyes_cascade
#
# face_cascade = cv.CascadeClassifier()
# eyes_cascade = cv.CascadeClassifier()
#
# #-- 1. Load the cascades
# if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
#     print('--(!)Error loading face cascade')
#     exit(0)
# if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
#     print('--(!)Error loading eyes cascade')
#     exit(0)
#
# camera_device = args.camera
# #-- 2. Read the video stream
# cap = cv.VideoCapture(camera_device)
# if not cap.isOpened:
#     print('--(!)Error opening video capture')
#     exit(0)
#
# while True:
#     ret, frame = cap.read()
#     if frame is None:
#         print('--(!) No captured frame -- Break!')
#         break
#
#     detectAndDisplay(frame)
#
#     if cv.waitKey(10) == 27:
#         break