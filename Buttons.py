from tkinter import *

root = Tk()


def myClick():
    my_label = Label(root, text="I am clicked!",fg='brown')
    my_label.pack()


button = Button(root, text="Click Me", command=myClick, fg='cyan', bg='#787777')
button.pack()

root.mainloop()
