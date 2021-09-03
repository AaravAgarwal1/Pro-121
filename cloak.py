
import cv2
import time
import numpy as np


fourcc= cv2.VideoWriter_fourcc(*'XVID') #video codec
output_file= cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480)) #width and height of the vid
cap=cv2.VideoCapture(0) #read the video

time.sleep(2) #allow the webcame to start by making the code to sleep for 2 seconds
bg= 0

for i in range(60):
    ret,bg=cap.read() #capturing the bg for 60 seconds

bg=np.flip(bg,axis=1) #flipping the video bcz cam captures image inverted

while(cap.isOpened()): #using the isOpened to check whether is opened or not
    ret,img=cap.read() #ret returns the booleans value of true or false whether cam is open or not
    if not ret:
        break 
    img=np.flip(img,axis=1) #flipping the img
    hsv=cv2.cvtColor(img,cv2.COLOR_BGRTOHSV) #converting the colors to rgb to hsv (hue saturating value)
    lower_red=np.array([0,120,50]) #creating the mask to detect any color of choice
    upper_red=np.array([10,255,255]) #color code
    mask_1= cv2.inRange(hsv,lower_red,upper_red) #creating mask 1 for detecting red color
    lower_red= np.array([170,120,70])
    upper_red=np.array([180,255,255])
    mask_2=cv2.inRange(hsv,lower_red,upper_red) #mask 2
    mask_1= mask_1+mask_2 #combining the masks in one
    mask_1= cv2.morphologyEx(mask_1,cv2.MORPH_OPEN, np.ones((3,3),np.uint8)) #parameters mask_1 is source, next is operation, next is matrix
    mask_1=cv2.morphologyEx(mask_1,cv2.MORPH_DILATE, np.ones((3,3),np.uint8)) #adding dilate effect
    mask_2=cv2.bitwise_not(mask_1) #select only the part which does not hv mask 1 and saving in mask 2
    res_1=cv2.bitwise_and(img,img,mask=mask_2) #creating resolution, img without color red 
    res_2=cv2.bitwise_and(bg,bg,mask=mask_1)#bg with bg we captured earlier
    final_output= cv2.addWeighted(res_1,1,res_2,1,0) #merging res_1 and res_2, adding both resolutions to the final output
    output_file.write(final_output)
    cv2.imshow("magic",final_output) #the name
    cv2.waitKey(1)

cap.release()
out.release()
cv2.destroyAllWindows()






