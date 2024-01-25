
import cv2 
import numpy as np
#from ffpyplayer.player import MediaPlayer
cap=cv2.VideoCapture("C:\\Users\\Swan Computers\\.vscode\extensions\\vehicle.MP4")

#car=cv2.CascadeClassifier("C:\\Users\\Swan Computers\\Documents\\python.ex\\myenv\\Lib\\site-packages\\cv2\\cars.xml")
#player=MediaPlayer("C:\\Users\\Swan Computers\\.vscode\extensions\\vehicle.MP4")
''' The process of removing the background from a given image and displaying 
only the foreground objects is called background subtraction in OpenCV, '''
algo=cv2.createBackgroundSubtractorMOG2()
min_width=80
min_hight=80
line_pos1=550 # window k oper line kahan le k aani h
line_pos2=540

#center_cordinate 
def center(x,y,w,h):
    x1=int(w/2)
    y1=int(w/2)
    cx=x+x1
    cy=y+y1
    return cx,cy

detect1=[]
detect2=[]
offset=6#allowed error to pixel
counter_1=0
counter_2=0
count_max=7
stop_direction=False
if(cap.isOpened()==False):
    print("check the error file not opened ")
while cap.isOpened():
  ret,frame=cap.read()
  ret
  #audio_frame,val=player.get_frame()
  
  gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  blur=cv2.GaussianBlur(gray,(3,3),5)

  sub_vid=algo.apply(blur)
  dilated=cv2.dilate(sub_vid,np.ones((5,5)))
  ''' It is rectangular shape. But in some cases, you may need elliptical/circular 
  shaped kernels. So for this purpose, OpenCV has a function, cv2.getStructuringElement(). 
  You just pass the shape and size of the kernel, you get the desired kernel.'''
  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
  '''  morphological  is broad set of image processing operations thata process binary image 
based on structuring element or kernal which decided the nature of operation 
in morphological opertaion each pixel in the image is adjusted based on the value of other pixel in its neighborhood 
 opening :  ersion followed by dilation " many time used in noise remove mask binary image hoti hai agr hum ne backgroud se impurity ko
 remove krna hai   
is mein hum phle ersion opertion apply krte hn jis se backgroup k white color remove ho jay ga 
 or bad mein dilation apply kr dein gaay 
 syntax: cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
  '''
  closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
  # again apply the closing morphological 
  closing=cv2.morphologyEx(closing, cv2.MORPH_CLOSE, kernel)
 
  count,h=cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  cv2.line(frame,(25,line_pos1),(500,line_pos1),(0,0,255),3)
  cv2.line(frame,(600,line_pos2),(1200,line_pos2),(0,0,255),3)
  ''' Enumerate() method adds a counter to an iterable and returns it in a form 
  of enumerating object. This enumerated object can then be used directly for loops 
  enumerate(iterable, start=0)
  '''
  
  for (i,c) in enumerate(count):
    
      (x,y,w,h)=cv2.boundingRect(c)
      #is k mutlab hai rec k ki width or hight itne honi chahitye 
      vildate_count=(w>=min_width) and (h>=min_hight)
      if not vildate_count:
          continue
      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
      #center cordinate function 
      ce=center(x,y,w,h)
      
      detect1.append(ce)

      cv2.circle(frame,ce,4,(0,0,255),-1)





      

       
      for (x,y) in detect1:# y is liye aay ga q k hum ne vartical hona h
          
          if y<(line_pos1+offset) and y>(line_pos1-offset) :
               counter_1+=1
             
               
               
          cv2.line(frame,(25,line_pos1),(500,line_pos1),(0,255,0),3)
          if y<(line_pos2+offset )and y>(line_pos2-offset):
              counter_2+=1

          
          
          #cv2.line(frame,(25,line_pos1),(500,line_pos1),(0,255,0),3)
          cv2.line(frame,(600,line_pos2),(1200,line_pos2),(0,255,0),3)
          
          detect1.remove((x,y))
          print("vehicle car"+str(counter_1))
          print("vehicle car"+str(counter_2))
  #cv2.putText(frame,'vehicle counter:'+str(counter_1),(450,70),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),5)
      cv2.putText(frame, f'Direction 1: {counter_1}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
      cv2.putText(frame, f'Direction 2: {counter_2}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# 2nd way 




      cv2.imshow('video',frame)
      if cv2.waitKey(1)==ord('q'):
         break
cap.release()
cv2.destroyAllWindows()

    
     



