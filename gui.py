from Tkinter import *
import datetime
import winsound
import time
import threading

class pomodoro(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.minsize(width=500, height=500)
        self.button = Button(self, text="Start", font = ("Verdana",18),
                             bg="Orange",command=self.handle_work)
        self.button.pack(side=LEFT, padx=10)
        self.slogan = Button(self,text="Stop", font = ("Verdana",18),
                             bg = "Cyan" ,command=self.reset)
        self.slogan.pack(side=LEFT, padx=10)

        #FOR TESTING

        self.candy = Button(self, text="Candy", font = ("Verdana",18),
                            bg="Purple",command=self.feed_me)
        self.candy.pack(side=LEFT, padx=10)

        self.spacing = Label(self, text="Timer :", font = ("Verdana",18), width=10)
        self.spacing.pack(side=TOP)

        self.label = Label(self, text="", font = ("Verdana",18), width=10)
        self.label.pack(side=TOP)
        
        self.title("STUDI-BOT")
        self.beeps()
        self.label.pack()
        self.minute = 0
        self.second = 0
        self.setup()
        #self.work()

    def beeps(self):
        freq = 2500
        dur = 300
        winsound.Beep(freq,dur)
        winsound.Beep(freq,dur)
        winsound.Beep(freq,dur)
        time.sleep(1)

    def updateString(self):
        self.label.configure(text="%d %d" % (self.minute, self.second))

    def setup(self):
        self.minute = 25
        self.second = 0
        self.updateString()

    def handle_work(self):
        self.w = threading.Thread(target=self.work_thread)
        self.w.start()

    def work_thread(self):
        try:
            self.work()
        except:
            print("Caught")
            self.minute = 25
            self.second = 0
            self.updateString()
            
        return

    def work(self):
        print("Started...")
        self.stop = False
        minutes = 1
        counter = 60
        current = minutes
        for i in range(minutes * 60):
            time.sleep(1)
            counter -= 1
            if counter == 0:
                counter = 60
                current -= 1
                print("Minute:",current)
            self.minute = current
            self.second = counter
            self.updateString()
            if self.stop == True:
                raise Exception
        print(current,":",counter)
        print("Break time!")
        self.beeps()

        self.feed_me()

        minutes = 4
        counter = 60
        current = minutes
        for i in range(minutes * 60):
            time.sleep(1)
            counter -= 1
            if counter == 0:
                current -= 1
                counter = 60
            self.minute = current
            self.second = counter
            self.updateString()
            if self.stop == True:
                raise Exception
        print("Work time!")
        self.beeps()
        return

    def reset(self):
        self.stop = True
        self.minute = 25
        self.second = 0
        self.updateString()
        return

    def feed_me(self):

        print("Feed me canddyyy")
        time.sleep(7)
        return
        

if __name__ == "__main__":
    app = pomodoro()
    app.mainloop()
