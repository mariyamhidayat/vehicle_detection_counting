import cv2
import numpy as np 
from ffpyplayer.player import MediaPlayer

cap=cv2.VideoCapture("C:\\Users\\Swan Computers\\.vscode\extensions\\vehicle.MP4")
player=MediaPlayer("C:\\Users\\Swan Computers\\.vscode\extensions\\vehicle.MP4")
car=cv2.CascadeClassifier("C:\\Users\\Swan Computers\\Documents\\python.ex\\myenv\\Lib\\site-packages\\cv2\\cars.xml")
if (cap.isOpened()== False):
    
    print("Error opening video file")
while(cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()
    audio_frame,val=player.get_frame()
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    c=car.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in c:
            
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            #We pass slice instead of index like this: [start:end].
            bro=cv2.copyMakeBorder(frame,10,10,10,10,cv2.BORDER_CONSTANT)
            
            if ret ==True:
                    cv2.imshow('Frame', bro)
                    if cv2.waitKey(1)== ord('q'):
                       break
            
          
            else:
                  break
cap.release()
  
# Closes all the frames
cv2.destroyAllWindows()
