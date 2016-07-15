#######################################################################
#Author: Megan Zimmerman                                              #
#File: guiforarduino.py                                               #
#Description:                                                         #
#    This program is a gui controller for a custom robotic arm using  #
# an Arduino UNO and two continuous rotation servos. Communication to #
# the arduino is done via the serial package, and all of the gui      #
# Attributes are derived from Tkinter and tk Canvas and fileDialog.   #
#                                                                     #
# if you have any questions about this code feel free to email me at  #
# zimmer1@umbc.edu or meganleahzimmerman@gmail.com                    #
#######################################################################

import Tkinter 
import serial
import time
import tkFileDialog


ser = serial.Serial('COM4', 9600)
time.sleep(2)

ser.write('13')

#Functions for writing operations to the Arduino through Serial
def OpenClaw():
    global ser
    ser.write('5')
    return

def CloseClaw():
    global ser
    ser.write('7')
    return

def upArm():
    global ser
    ser.write('2')
    return

def downArm():
    global ser
    ser.write('3')
    return

def grab():
    global ser
    ser.write('13')
    return

#initializing the gui window
win = Tkinter.Tk()
win.minsize(width=500,height=500)
draw = Tkinter.Canvas(win,width=500,height=500,bg="#9BA7C2")
draw.pack()

#global variables for the opperation loops to controll off of
global upmove
upmove = 0
global currentKey
global downmove


#loop for continous update in the upward direction
def upButton(event):
    print("doing thing")
    global upmove
    global currentKey
    currentkey= 1
    upmove = 1
    gogo = 1
    if gogo == 1:
        upLoop()
        gogo=2

#Calling the serial function for the loop in UpButton
def upLoop():
    global upmove
    global possition
    print("going")
    upArm()
    possition +=1
    print ('in up', possition)

#For the end of the UpButton loop
def upStop():
    global upmove
    upmove = 0

#Essentially the same things happening here but in the downwards direction
def downButton(event):
    global currentKey
    currentkey= 0
    global downmove
    downmove = 1
    gogo = 1
    if gogo == 1:
        downLoop()
        gogo=2

#Calling serial function and updating the global possition variable
def downLoop():
    global possition
    global downmove
    print("going")
    downArm()
    possition -=1
    print('in down', possition)

#For the end of the DownButton loop
def downStop():
    global downmove
    downmove = 0

#Stopping all actions
def stopit(event):
    upStop()
    downStop()

#Global variables for keeping track of the up or down status
global up
global down
possition = 0
isopen = False

#Loading a file
def chooseFileDialog():
    global isopen
    global possition
    
    #using the tkFileDialog to open a file via a gui
    file = tkFileDialog.askopenfile(parent = win, mode = 'rb', title='select a file')

    if file != None:
        currentName = file
        #Extracting the possition and the gripper data from the file
        newpos = int(file.readline().strip())
        gripper = int(file.readline().strip())
        print("new pos",newpos,"   gripper",gripper)
        flag = False
        pos1 = newpos
        #Adjusting the robot possition to the new possition
        while pos1 != possition:
            if pos1 < possition:
                downArm()
                possition -=1
                print(possition, " going down")
            if pos1 > possition:
                upArm()
                possition +=1
                print(possition, "going up")
                
        #Changing the gripper status if need be
        if gripper == 1 and isopen == False:
            OpenClaw()
        elif gripper == 0 and isopen == True:
            CloseClaw()

#Using TKFileDialog to save the file            
def onSaveAs():
    global isopen
    file = tkFileDialog.asksaveasfile(mode='w')
    
    if file !=None:
        #Writing the possition and the status of the gripper
        file.write(str(possition))
        file.write("\n")
        if isopen == False:
            file.write('0')
        else:
            file.write('1')
        file.close()

        
def motion(event):
    global isopen
    global possition
    global up
    global down
    contained1 = False
    contained2 = False
    print("Mouse position: (%s %s)" % (event.x, event.y))

    #Up button contained
    if (event.x<150 and event.x>51 and event.y < 172 and event.y > 70):
        print "contained"
        upArm()
        possition +=1
        contained1 = True
        print(possition)
        
    #Down button contained
    if (event.x<150 and event.x>51 and event.y < 300 and event.y > 200):
        contained2 = True
        downArm()
        possition -=1
        print "2"

    #Close button containment
    if (event.x<450 and event.x>351 and event.y < 300 and event.y > 200):
        if isopen == True:
            CloseClaw()
            isopen = False
        print "close"

    #Open button containment
    if (event.x<450 and event.x>351 and event.y < 172 and event.y > 70):
        if isopen ==False:
            OpenClaw()
            isopen =True
        print "open"

    #Grab button containment
    if (event.x<299 and event.x>190 and event.y < 440 and event.y > 341):
        grab()
        print "grab"

    #Load button containment
    if (event.x<439 and event.x>372 and event.y < 451 and event.y >423 ):
        chooseFileDialog()
        print "load"

    #Save button containment
    if (event.x<439 and event.x>372 and event.y <487  and event.y >456 ):
        print "save"
        onSaveAs()
        
    return

#Function for ease of circle creation
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)


Tkinter.Canvas.create_circle = _create_circle
#Values for the UI colors, for easy formating in variables
strgre = "#236A68"
strblue = "#2A4F6E"
labelblue = "#02192C"
labellgreen = "#0A4E4B"
textcolor = "#041332"

#Up buttons
draw.create_circle(100, 120, 50, fill=strgre, outline=labellgreen)
draw.create_circle(100, 250, 50, fill=strgre, outline=labellgreen)

#Down buttons
draw.create_circle(400, 120, 50, fill=strgre, outline=labellgreen)
draw.create_circle(400, 250, 50, fill=strgre, outline=labellgreen)

#Gripper button
draw.create_rectangle(  300, 340, 190, 440, fill=strblue, outline=labelblue)

#Adding the labels on all of the buttons
draw.create_text(99,127,fill=textcolor,text="^", font=('Arial', 70, 'bold'))
draw.create_text(99,251,fill=textcolor,text="v", font=('Arial', 55, 'bold'))
draw.create_text(94,36,fill=textcolor,text="Arm Possition", font=('Arial', 17, 'bold'))
draw.create_text(400,118,fill=textcolor,text="Open", font=('Arial', 20, 'bold'))
draw.create_text(400,248,fill=textcolor,text="Close", font=('Arial', 20, 'bold'))
draw.create_text(399,36,fill=textcolor,text="Gripper", font=('Arial', 17, 'bold'))
draw.create_text(244,388,fill=textcolor,text="Grasp", font=('Arial', 17, 'bold'))

#Adding the save button
draw.create_rectangle(  372, 457, 439, 487, fill=strblue, outline=labelblue)
draw.create_text(404,472,fill=textcolor,text="Save", font=('Arial', 15, 'bold'))

#Adding the load button
draw.create_rectangle(  372, 422, 439, 452, fill=strblue, outline=labelblue)
draw.create_text(404,437,fill=textcolor,text="Load", font=('Arial', 15, 'bold'))

#For use of the buttons with the gui
draw.bind('<Button>',motion)
win.bind('<Up>',upButton)
win.bind('<Down>',downButton)
win.bind('<Any-KeyRelease>',stopit)

#More text formating
win.wm_title("Custom Arm Control")
label1 = Tkinter.Label(win, text="or press up and down keys to control motion")

#Adding the label to the pack and running the window
label1.pack()
win.mainloop()

