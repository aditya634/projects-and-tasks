from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

# Geometry of my application
root.geometry("500x500")

# Title for my application
root.title("Travels Forms")

root.config(bg="white")

def giveMsg():
    print("Form Submitted !!")
    print(f"You have rated {myslider2.get()}\nThank You !!")
    tmsg.showinfo("Rating",f"You have rated {myslider2.get()}\nThank You !!")
    data = f"Name : {userName.get()}\nPhone : {userPhone.get()}\nGender : {userGender.get()}\nEmergency Contact : {userEmergency.get()}\nPaymentMode : {userPaymentMode.get()}\nPreMeals Services : {userFoodService.get()}\nFood : {Choice.get()}\nRating : {myslider2.get()}"
    tmsg.showinfo("Your Data !!",data)
    

# Add your Widgets here
# Using One Liner 
# Heading for the Form :
heading = Label(root,bg="white",font="Ubuntu 20 bold",text="Welcome To Sanjay Travels")
heading.grid(row=0,column=3)

# Labels for the form
name = Label(root,bg="white",font="Ubuntu 15 bold",text="Name : ")
name.grid(row=1,column=2,sticky=E,padx=10,pady=10)
phone = Label(root,bg="white",font="Ubuntu 15 bold",text="Phone : ")
phone.grid(row=2,column=2,sticky=E,padx=10,pady=10)
gender = Label(root,bg="white",font="Ubuntu 15 bold",text="Gender : ")
gender.grid(row=3,column=2,sticky=E,padx=10,pady=10)
emergency  = Label(root,bg="white",font="Ubuntu 15 bold",text="Emergency Contact : ")
emergency.grid(row=4,column=2,sticky=E,padx=10,pady=10)
paymentMode = Label(root,bg="white",font="Ubuntu 15 bold",text="PaymentMode : ")
paymentMode.grid(row=5,column=2,sticky=E,padx=10,pady=10)
Food = Label(root,bg="white",font="Ubuntu 15 bold",text="Food : ",padx=10)
Food.grid(row=8,column=2,sticky=E)

# StringVar variables :
userName = StringVar()
userPhone = StringVar()
userGender = StringVar()
userEmergency = StringVar()
userPaymentMode = StringVar()
userFoodService = IntVar()
Choice = StringVar()
# Choice.set("idle")
Choice.set(None)

# Entries
nameEntry = Entry(root,bg="white",textvariable=userName,font="Ubuntu 15 bold")
nameEntry.grid(row=1,column=3,sticky=W,padx=10,pady=10)
phoneEntry = Entry(root,bg="white",textvariable=userPhone,font="Ubuntu 15 bold")
phoneEntry.grid(row=2,column=3,sticky=W,padx=10,pady=10)
genderEntry = Entry(root,bg="white",textvariable=userGender,font="Ubuntu 15 bold")
genderEntry.grid(row=3,column=3,sticky=W,padx=10,pady=10)
emergencyEntry = Entry(root,bg="white",textvariable=userEmergency,font="Ubuntu 15 bold")
emergencyEntry.grid(row=4,column=3,sticky=W,padx=10,pady=10)
paymentEntry = Entry(root,bg="white",textvariable=userPaymentMode,font="Ubuntu 15 bold")
paymentEntry.grid(row=5,column=3,sticky=W,padx=10,pady=10)

# Radiobuttons :
radio1 = Radiobutton(root,bg="white",text="Dosa",padx=20,variable=Choice,value="Dosa",font="Ubuntu 15 bold")
radio1.grid(row=6,column=3,sticky=W)
radio2 = Radiobutton(root,bg="white",text="Idle",padx=20,variable=Choice,value="Idle",font="Ubuntu 15 bold")
radio2.grid(row=7,column=3,sticky=W)
radio3 = Radiobutton(root,bg="white",text="Samosa",padx=20,variable=Choice,value="Samosa",font="Ubuntu 15 bold")
radio3.grid(row=8,column=3,sticky=W)
radio4 = Radiobutton(root,bg="white",text="Paneer Paratha",padx=20,variable=Choice,value="Paneer Paratha",font="Ubuntu 15 bold")
radio4.grid(row=9,column=3,sticky=W)

rate=Label(root,bg="white",text="Rate you Experience :",font="Ubuntu 15 bold")
rate.grid(row=10,column=2,sticky=E,padx=10,pady=10)

# Slider in Horizontal Direction
myslider2 = Scale(root,bg="white",activebackground="red",highlightbackground="yellow",from_=0,to=50,orient=HORIZONTAL,length=500,tickinterval=2)
myslider2.grid(row=10,column=3,sticky=W,padx=10,pady=10)

# To connect scrollbar to a widget
# Step 1 : widget(yscrollcommand = scrollbar.set)
# Step 2 : scrollbar.config(command=widget.yview)

# Adding Scrollbar to the Text:
Text_ScrollBar = Scrollbar(root,orient=VERTICAL,borderwidth=3)

Label(root,bg="white",text="Feedback :",font="Ubuntu 15 bold").grid(row=11,column=2,sticky=E,padx=10,pady=10)

Text1 = Text(root,yscrollcommand=Text_ScrollBar.set,height=5)
Text_ScrollBar.grid(row=11,column=4,sticky=N+S+W)

Text1.grid(row=11,column=3,padx=10,pady=20,sticky=W)
Text_ScrollBar.config(command=Text1.yview)

# Checkboxes :
foodServices = Checkbutton(text="Want to Prebook your Meals ?",bg="white",variable=userFoodService,font="Ubuntu 15 bold")
foodServices.grid(row=12,column=3,sticky=W,padx=10,pady=10)

# Submit Button : 
submitbtn = Button(root,bg="pink",text="Submit Now",command=giveMsg,font="Ubuntu 15 bold")
submitbtn.grid(row=13,column=3,padx=10,pady=10)

def filemenu():
    print("This is a file Menu . . . ")
def openmenu():
    print("This is a open Menu . . . ")
def savemenu():
    print("This is a save Menu . . . ")
def saveAsmenu():
    print("This is a saveAs Menu . . . ")

def darkmode():
    root.config(bg="black")

def lightmode():
    root.config(bg="#f0f0f0")

def messages():
    msg1 = tmsg.showinfo("HELP","Sanjay will Help You !!")
    print(msg1)
    rating = tmsg.askquestion("Was you experience GOOD . . ?","You Used this GUI. . .  was your experience Good ?")
    print(rating)
    ans = tmsg.askretrycancel("Image","Image not Loaded Properly . . . .")
    print(ans)

msgboxbtn = Button(root,bg="pink",text="Message Boxes",command=messages,font="Ubuntu 15 bold")
msgboxbtn.grid(row=14,column=3,padx=10,pady=10)

# making a dropdown menu
dropDownMenu = Menu(root,bg="white")

# ------------->> Making a FILE Menu <<-------------
menuOption1 = Menu(dropDownMenu,tearoff=FALSE)
# making a list of options that will appear in dropdown :
menuOption1.add_command(label="New File",command=filemenu)
menuOption1.add_command(label="Open File",command=openmenu)
menuOption1.add_separator()     # Add a line Separator
menuOption1.add_command(label="Save",command=savemenu)
menuOption1.add_command(label="Save As",command=saveAsmenu)
menuOption1.add_separator()     # Add a line Separator
menuOption1.add_command(label="Dark Mode",command=darkmode)
menuOption1.add_command(label="Light Mode",command=lightmode)
menuOption1.add_separator()     # Add a line Separator
menuOption1.add_command(label="Exit",command=quit)
# To make a Menu Title :
dropDownMenu.add_cascade(label="File",menu=menuOption1)
# Making the Menu of our application as mymenu
root.config(menu=dropDownMenu)

# Making the Application run
root.mainloop()