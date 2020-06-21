import cv2
#import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('myFace720.mp4')
run = True
while run:
    ret, frame = cap.read()
    if ret:
        #frame = cv2.resize(frame, (850, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
            cv2.circle(frame, (x + int(w/2), y + int(h/2)), 3, (0,0,255), -1)
     
        cv2.imshow('res', frame)
    
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            run = False
            break
    else:
        run = False
        break


cv2.destroyWindow('res')
cap.release()