from tkinter import *

myWin = Tk()

myWin.title("My Application")

myWin.geometry("700x500")

# myWin.maxsize(300,300)
myWin.minsize(300,300)

IntroText1 = Label(myWin,text="This is a Label which contain Text in it")
IntroText1.pack()

myWin.mainloop()