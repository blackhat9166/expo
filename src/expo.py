from concurrent.futures import thread
import cv2
import time
import math
import datetime
import keyboard
import threading


h = 1
w = 1
n =1
cap = cv2.VideoCapture(0)
i_time = 0
p_time = 0
current_time = time.ctime()


while True:
    ret, frame = cap.read()
    
    font = cv2.FONT_HERSHEY_COMPLEX
    current_time = time.ctime()

    i_time = time.time()
    fps = int(1/(i_time-p_time))
    p_time = i_time
    fps = "fps = " + str(fps)  
    zoom = "Mx ="+str(n)
    ping = 'ping: xx'
    error = '1%'
    mode = 'NML'
    tempp = 'temp,pr: 23, 1.87'
    Re = 'psbl-1'
   

    img = cv2.line(frame, (0,240), (640,240), (0,0,0),thickness=1, lineType=8)
    img = cv2.line(frame, (320, 0), (320, 480), (0, 0, 0), thickness=1, lineType=8)
    img = cv2.line(frame, (320, 240+n*h), (640, 240+n*h), (255, 0, 0), thickness=1, lineType=8)
    img = cv2.line(frame, (320+n*w, 240), (320+n*w, 480), (255, 0, 0), thickness=1, lineType=8)
    img = cv2.putText(img, fps, (2, 10), font, 0.4, (100, 255, 0), 1, cv2.LINE_AA)
    img = cv2.putText(img, zoom, (2, 25), font, 0.4, (100, 255, 0), 1, cv2.LINE_AA)
    img = cv2.putText(img, current_time, (2, 470), font, 0.2, (100, 255, 0), 1, cv2.LINE_AA)
    img = cv2.putText(img, ping, (585, 10), font, 0.4, (100, 255, 0), 1, cv2.LINE_AA)
    img = cv2.putText(img, Re, (2, 435), font, 0.3, (100, 255, 0), 1, cv2.LINE_AA)
    img = cv2.putText(img, tempp, (2, 450), font, 0.2, (100, 255, 0), 1, cv2.LINE_AA)
    img = cv2.resize(img,(1200,800))
    
    if keyboard.is_pressed("z"):
     n += 1
    elif keyboard.is_pressed("o"):
     n -= 1
    cv2.imshow("video", img)
    

    if cv2.waitKey(1) & 0xff == ord('q'):
        break



