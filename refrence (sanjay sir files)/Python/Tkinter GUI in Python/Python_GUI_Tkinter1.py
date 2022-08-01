''' 
    # What is Tkinter ?
        -> Tkinter is a built-in Python module for developing a GUI application. 

    # Follow the three easy steps given below to create the main window:

        o Importing tkinter is the same as importing any other module in Python. Note that the module's name in Python 2.x is 'Tkinter,' and in Python 3.x, it is 'tkinter'.
            from tkinter import *

        o To create the main window, Tkinter offers a method, 'Tk'. To change the name of the window, you can change the className to the desired one.
            myWindow = Tk()

        o There is a method known by the name mainloop(), which is used when your application is ready to run. This is an infinite loop used to run the application, wait for an event to occur, and process the event as long as the window is not closed.
            myWindow.mainloop()

    # Widgets :
        -> Widgets are the basic building blocks for graphical user interface (GUI) applications.

    # There are mainly three geometry manager classes : 
        o pack() method :
            - It organizes the widgets in blocks before placing them in the parent widget.
        o grid() method :
            - Before placing them in the parent widget, it organizes the widgets in the grid (table-like structure).
        o place() method :
            - It organizes the widgets by placing them on specific positions directed by the programmer.
'''


from tkinter import *
from PIL import Image,ImageTk
# PIL : Photo Image Library

root = Tk()

# Setting Width and Height using geometry intiailly:
# Syntax : root.geometry("WidthxHeight")
root.geometry("1000x700")

# Setting the Application Name in the Title Bar :
root.title("My Application . . . ")


# Setting up the Minimum width and Height when User resizing so that whole window will not be hidden
# Syntax : root.minsize(Width,Height)
# root.minsize(500,500) 

# Setting up the Maximum width and Height while User resizing due to some reasons like not allowing to maximize the window, not to  change the design for the window ,etc . . . .
# Syntax : root.maxsize(Width,Height)
# root.maxsize(500,500)

# ------------------------------>> Adding Labels <<------------------------------
# Creating a Label
# IntroText1 = Label(root,text="This is a Label which contain Text in it")
# # If we not pack the widgets, we will not get that in output window !
# IntroText1.pack()

data = "This is a Sample data text We can \nadd what ever text we want "

myText = Label(text=data+"with red background", bg="red")
# myText.pack()
# myText = Label(text=data*2+"with red background and white text color", bg="red",fg="white")
# myText.pack()
# myText = Label(text=data*3+"with red background and white text color with 50 padx", bg="red",fg="white",padx=50)
# myText.pack()
# myText = Label(text=data*3+"with red background and white text color with 50 padx and 50 pady", bg="red",fg="white",padx=50,pady=50)
# myText.pack()
# myText = Label(text=data+"with red background and white text color with 50 padx\n and 50 pady and font size 10 Ubuntu bold", bg="red",fg="white",padx=50,pady=50,font=("Ubuntu 20 bold"))
# myText.pack()
# myText = Label(text=data+"with red background and white text color with 50 padx\n and 50 pady and font size 10 Ubuntu bold with borderwidth 10", bg="red",fg="white",padx=50,pady=50,font=("Ubuntu 10 bold"),borderwidth=10)
# myText.pack()
# myText = Label(text=data+"with red background and white text color with 100 padx\n and 100 pady and font size 10 Ubuntu bold with borderwidth 10 and relief SUNKEN", bg="red",fg="white",padx=100,pady=100,font=("Ubuntu 10 bold"),borderwidth=10,relief=SUNKEN)
# myText.pack()

# # ------------------------------>> Using pack() attributes <<------------------------------
# anchor : used to give direction
# myText.pack(anchor="ne") # North East
# myText.pack(anchor="nw") # North West

# myText.pack(anchor="se") # South East ==> It will not be in South East Direction
# # For that we have to add the SIDE attribute
# myText.pack(side=BOTTOM,anchor="sw")

# # # As we have some empty same in the left side
# # To fill the whole axis(horizontal,vertical) with the widget we use fill attribute
myText.pack(side=BOTTOM,anchor="se",fill=X)
myText.pack(side=LEFT,fill=Y)

# # # To add some Space on the sides
myText.pack(side=LEFT,fill=Y,padx=20,pady=20)


# ------------------------------>> Adding Images <<------------------------------
# Making a Photo using a PhotoImage class
photo = PhotoImage(file="Sanjay.png")

# We cannot directly add the image, we have to add it in label
label1 = Label(image=photo)
label1.pack()
label2 = Label(text="This is Logo of Sanjay Sukhwani !")
label2.pack()

# For jpg image files :
image_jpg = Image.open("img.jpg")

# Resizing the Image :
# image.resize((w, h)) : This command allows us to change the height(h) and width(w) of the image.
image_jpg = image_jpg.resize((300,200))

photoJPG = ImageTk.PhotoImage(image=image_jpg)
label3 = Label(image=photoJPG)
label3.pack()

# ------------------------------>> Adding Buttons <<------------------------------
def hello():
    print("Hello Tkinters !!")

    # 1st Way to get Message in Application
    # msg = Label(root,text="Login Successfull")
    # msg.pack()

    # 2nd Way :
    # msg2.config(text="Hello Tkinters !!",fg="red")

msg2 = Label(root)
msg2.pack()

b1 = Button(root,fg="Yellow",bg="black",text="Print Message",font="Ubuntu 13 bold",command=hello,activebackground="red",activeforeground="white",cursor="circle")
b1.pack(padx=20,pady=20)
# b1.pack(padx=20,pady=20,fill=X,anchor=CENTER)


root.mainloop()