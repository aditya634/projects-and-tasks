from tkinter import *

root = Tk()

# Geometry of my application
canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")

# Title for my application
root.title("My Application")

# Add your Widgets here
# Adding canvas widget :
# relief is same as border-style in css
canvasWidget = Canvas(root,bg="lightgreen",width=canvas_width,height=canvas_height,borderwidth=1,relief=SOLID)
canvasWidget.pack()

# Creating a Line in Canvas : 
# create_line(x1,y1,x2,y2) : The Line goes from (x1,y1) to (x2,y2)
canvasWidget.create_line(0,0,800,400)
canvasWidget.create_line(800,0,0,400)

# Creating a Rectangle in Canvas :
# create_rectangle(x1,y1,x2,y2) : Create rectangle with coordinates Top-Left Corner(x1,y1) and Bottom-Right Corner(x2,y2)
canvasWidget.create_rectangle(0,0,200,200,fill="pink")

# Creating a Text in Canvas :
# create_text(x1,y1,text="") : Create text at coordinates (x1,y1).
canvasWidget.create_text(400,400,text="Sanjay Sukhwani")

# Creating a Oval in Canvas :
# create_oval(x1,y1,x2,y2) : Create Oval inside a Rectangle with coordinates Top-Left Corner(x1,y1) and Bottom-Right Corner(x2,y2)
canvasWidget.create_oval(100,100,340,560,fill="red")

# Making the Application run
root.mainloop()