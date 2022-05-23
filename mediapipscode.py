from cProfile import label
import tkinter as tk 
from tkinter import *
from tkinter import ttk
from turtle import left, update 
from PIL import ImageTk, Image
import cv2
from matplotlib import image
import numpy as np
import mediapipe as mp
import time, datetime  #for delay functions
import microcontroller as mic
from ctypes.wintypes import RGB



#direction= "Down"
#----------------------




# def video_open():
#     global cap
#     cap = cv2.VideoCapture(0)

# video_open()

# def Arrow(direction):
#     global rightt,downn,leftt,upp,right,leftarrow,up,down
#     rightt= ImageTk.PhotoImage(Image.open("C:/Users/HP/Desktop/PICK ME CHOOSE ME/GUI_Python/lefty.jpg") )
#     downn= ImageTk.PhotoImage(Image.open("C:/Users/HP/Desktop/PICK ME CHOOSE ME/GUI_Python/arrow down.jpg") )
#     leftt= ImageTk.PhotoImage(Image.open("C:/Users/HP/Desktop\PICK ME CHOOSE ME/GUI_Python/arrow up.jpg") )
#     upp= ImageTk.PhotoImage(Image.open("C:/Users/HP/Desktop/PICK ME CHOOSE ME/GUI_Python/arrow up.jpg") )
    
#     if (direction== "Right"):
#         rightt= ImageTk.PhotoImage(Image.open("y-right.jpg") ) 

#     elif (direction == "Left"):       
#         leftt= ImageTk.PhotoImage(Image.open("y-left.jpg") )
#     elif (direction== "Up"):
#         upp= ImageTk.PhotoImage(Image.open("y-up.jpg") )
#     elif (direction== "Down"):
#         downn= ImageTk.PhotoImage(Image.open("y-down.jpg") )       
    
#     right=Label(image=rightt)
#     right.place(relx = 0.97,
#                   rely = 0.90,
#                   anchor ='se')
    
#     down=Label(image=downn)
#     down.place(relx = 0.92,
#                     rely = 0.99,
#                     anchor ='se')
    
#     leftarrow=Label(image=leftt)
#     leftarrow.place(relx = 0.895,
#                     rely = 0.90,
#                     anchor ='se')
    
    
#     up=Label(image=upp)
#     up.place(relx = 0.895,
#                     rely = 0.76)




##########################################

window = Tk()
window.title("RoboCar control using Hand Gestures")
window.configure(bg = "pink")
titleba = Label(window, text="Gestured control RC car", font=("Calibri",30), bg="pink", 
            fg="Maroon", relief=GROOVE).place(relx=0.5,rely=0.1, anchor ="center")

# titleba = Label(window, text="All rights reserved to Zainab n Noor e jan", font=("Modern No. 20",50,"bold"), bg="gray", fg="Maroon", relief=GROOVE).place(relx=0.5,rely=0.1, anchor ="center")

f1= LabelFrame(window, bg="red").place(relx=0.5,rely=0.5) #this is vid background
L1 = Label(f1, height = 500 , width = 660 ,bg="maroon")
L1.place(relx=0.5,rely=0.5, anchor = 'center') #ive placed it in center and u can change color too



Label(window,text="Choose your video:",font=("Calibri",25),bg="pink").place(relx=0.05,rely=0.2) # here is the label corner

v=StringVar()
str(v.get())

VIDEOS=[("Play vid1","Handgesturevid1.mp4",0.05,0.3),
        ("Play vid2","handgesturevid2.mkv",0.05,0.35)
]

Label(window,text="2020-MC-19 Zainab Ishtiaq",font=("Calibri",20),bg="pink").place(relx=0.75,rely=0.2)
Label(window,text="2020-MC-35 NoorUlAein",font=("Calibri",20),bg="pink").place(relx=0.75,rely=0.25)
#---------------------
vidadd=StringVar() # will have to make a function with main loop so it doesnt crash, chech izzi;s code
vidadd.set("Handgesturevid1.mp4") #settin default video
livevar=IntVar() #variable for live vid too, this depends on ur computer camera
livevar.set(0)

#---------------------this is for selecting vid
def video_click(address):
    global cap
    #Label(win,text=address).place(x=700,y=500) # To check adress
    if address==0:
        cap = cv2.VideoCapture(0)
        vidadd.set(" ")
    else:
        vidadd.set(address)
        cap = cv2.VideoCapture(vidadd.get())

global direction
direction = 'Up'

# for our radiobuttton
for name,address,x,y in VIDEOS:
    Radiobutton(window,text=name,variable=vidadd,value=address).place(relx=x,rely=y)

# Live and Recorded video switching and placement   
Button(window,text="Select",bg="white",command=lambda:video_click(vidadd.get())).place(relx=0.05,rely=0.4)
Button(window,text="Open Webcam",bg="yellow",fg="black",command=lambda:video_click(livevar.get())).place(relx=0.05,rely=0.5)

#for display, this will need to be configured by gicing some def in command, use arrow function
# directionbox = Label(window,width=50,borderwidth=5,textvariable= direction, font= ("Calibri Bold",25),bg="white" ,relief=GROOVE).place(relx= 0.85 , rely = 0.4, height = 50 , width = 300, anchor = 'center')
#text variable
#------------------for destroying windows
def close():
    window.destroy()
#exit button 
Button(f1, text="Exit the Application", bg='#fffdd0', fg='black', font=("Calibri", 14, "bold"), command=close).place(relx=0.11, rely=0.8, anchor ="center")
#------------------
#cap = cv2.VideoCapture(vidadd.get())
####################################
   

mp_draw=mp.solutions.drawing_utils
mp_hand=mp.solutions.hands

tipIds=[4,8,12,16,20]
# bottomtips =[1,5,9,13,17]


hands = mp_hand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture("Handgesturevid1.mp4")

#cap = cv2.VideoCapture("WIN_20220510_14_09_49_Pro.mp4")
def Video():

        
        ret,img=cap.read()
        # img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # img.flags.writeable=False
        results=hands.process(img)
        img.flags.writeable=True
        img=cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        lmList=[]
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands=results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h,w,c=img.shape
                    cx,cy= int(lm.x*w), int(lm.y*h)
                    lmList.append([id,cx,cy])
                mp_draw.draw_landmarks(img, hand_landmark, mp_hand.HAND_CONNECTIONS)

        fingers=[]
        if len(lmList)!=0:
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            total=fingers.count(1)

            direction = mic.RCCAR(total)
         


            if total==0:
            
                cv2.putText(img, "BRAKE", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                print("brake")
            

            if total==5:

                cv2.putText(img, " FORWARD", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                print("forward")

            if total==2:

                cv2.putText(img, " RIGHT", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                print("right")


            if total==3:
                #cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, " LEFT", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                print("left")

            if total==4:
                #cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, "REVERSE", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                print("REVERSE")


            #cv2.imshow("Frame",image)
            k=cv2.waitKey(1)
            # if k==ord('q'):
            #     break

        return img
        #####################
        

def select_img():
    image = Image.fromarray(Video())
    finalImage = ImageTk.PhotoImage(image)
    L1.configure(image=finalImage)
    L1.image = finalImage
    window.after(1, select_img)

select_img()

window.mainloop()
