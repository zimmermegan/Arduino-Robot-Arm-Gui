import Tkinter 
import serial
import time
import tkFileDialog


ser = serial.Serial('COM4', 9600)
time.sleep(2)

ser.write('13')
#ser = ""
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
win = Tkinter.Tk()
win.minsize(width=500,height=500)
draw = Tkinter.Canvas(win,width=500,height=500,bg="#9BA7C2")
draw.pack()
global upmove
upmove = 0
global currentKey
global downmove
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


def upLoop():
    global upmove
    global possition
    print("going")
    upArm()
    possition +=1
    print ('in up', possition)

def upStop():
    global upmove
    upmove = 0

def downButton(event):
    global currentKey
    currentkey= 0
    global downmove
    downmove = 1
    gogo = 1
    if gogo == 1:
        downLoop()
        gogo=2


def downLoop():
    global possition

    global downmove

    print("going")
    downArm()
    possition -=1
    print('in down', possition)

def downStop():
    global downmove
    downmove = 0

def stopit(event):
    upStop()
    downStop()

global up
var = "blue"
global down
small = "pink"
possition = 0
isopen = False
def chooseFileDialog():
    global isopen
    global possition
    file = tkFileDialog.askopenfile(parent = win, mode = 'rb', title='select a file')
    if file != None:
        currentName = file
        newpos = int(file.readline().strip())
        
        gripper = int(file.readline().strip())
        print("new pos",newpos,"   gripper",gripper)
        flag = False
        pos1 = newpos
        while pos1 != possition:
            if pos1 < possition:
                downArm()
                possition -=1
                print(possition, " going down")
            if pos1 > possition:
                upArm()
                possition +=1
                print(possition, "going up")
        if gripper == 1 and isopen == False:
            OpenClaw()
        elif gripper == 0 and isopen == True:
            CloseClaw()
def onSaveAs():
    global isopen
    file = tkFileDialog.asksaveasfile(mode='w')
    if file !=None:
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
    #top button contained
    if (event.x<150 and event.x>51 and event.y < 172 and event.y > 70):
        print "contained"
        upArm()
        possition +=1
        contained1 = True
        print(possition)
    if (event.x<150 and event.x>51 and event.y < 300 and event.y > 200):
        contained2 = True
        downArm()
        possition -=1
        print "2"
    if (event.x<450 and event.x>351 and event.y < 300 and event.y > 200):
        #CloseGrip()
        if isopen == True:
            CloseClaw()
            isopen = False
        print "close"
    if (event.x<450 and event.x>351 and event.y < 172 and event.y > 70):
        if isopen ==False:
            OpenClaw()
            isopen =True
        #OpenGrip()
        print "open"
    if (event.x<299 and event.x>190 and event.y < 440 and event.y > 341):
        grab()
        print "grab"
    if (event.x<439 and event.x>372 and event.y < 451 and event.y >423 ):
        chooseFileDialog()
        print "load"
    if (event.x<439 and event.x>372 and event.y <487  and event.y >456 ):
        print "save"
        onSaveAs()
    return

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Tkinter.Canvas.create_circle = _create_circle
strgre = "#236A68"
strblue = "#2A4F6E"
labelblue = "#02192C"
labellgreen = "#0A4E4B"
textcolor = "#041332"

draw.create_circle(100, 120, 50, fill=strgre, outline=labellgreen)
draw.create_circle(100, 250, 50, fill=strgre, outline=labellgreen)

draw.create_circle(400, 120, 50, fill=strgre, outline=labellgreen)
draw.create_circle(400, 250, 50, fill=strgre, outline=labellgreen)

draw.create_rectangle(  300, 340, 190, 440, fill=strblue, outline=labelblue)
draw.create_text(99,127,fill=textcolor,text="^", font=('Arial', 70, 'bold'))
draw.create_text(99,251,fill=textcolor,text="v", font=('Arial', 55, 'bold'))
draw.create_text(94,36,fill=textcolor,text="Arm Possition", font=('Arial', 17, 'bold'))
draw.create_text(400,118,fill=textcolor,text="Open", font=('Arial', 20, 'bold'))
draw.create_text(400,248,fill=textcolor,text="Close", font=('Arial', 20, 'bold'))
draw.create_text(399,36,fill=textcolor,text="Gripper", font=('Arial', 17, 'bold'))
draw.create_text(244,388,fill=textcolor,text="Grasp", font=('Arial', 17, 'bold'))

draw.create_rectangle(  372, 457, 439, 487, fill=strblue, outline=labelblue)
draw.create_text(404,472,fill=textcolor,text="Save", font=('Arial', 15, 'bold'))

draw.create_rectangle(  372, 422, 439, 452, fill=strblue, outline=labelblue)
draw.create_text(404,437,fill=textcolor,text="Load", font=('Arial', 15, 'bold'))

#draw.create_rectangle( 175,  318, 90, 85, fill="orange", outline = "black")
#draw.create_rectangle( 50, 100, 150, 200, fill="green", outline="red", width=3)
#draw.create_rectangle(125,  25, 175, 190, fill="purple", width=0)
draw.bind('<Button>',motion)
win.bind('<Up>',upButton)
win.bind('<Down>',downButton)

win.bind('<Any-KeyRelease>',stopit)

win.wm_title("Custom Arm Control")

label1 = Tkinter.Label(win, text="or press up and down keys to control motion")
label1.pack()
win.mainloop()

