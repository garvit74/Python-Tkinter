from tkinter import *

root = Tk()
e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Name: ")


def myClick():
    hello = f"Hello! {e.get()}"
    my_label = Label(root, text=hello, fg='brown')
    my_label.pack()


button = Button(root, text="Enter Your Name", command=myClick, fg='white', bg='sky blue')
button.pack()

root.mainloop()
