from tkinter import *

root = Tk()

# Creating a label

myLabel1 = Label(root, text="Hello World!")

myLabel2 = Label(root, text="My name is Garvit Agrawal")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)


root.mainloop()

