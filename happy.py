from tkinter import *



root = Tk()
root.title("Graphic")
root.geometry("800x800")





lbel = Label(root, text = "first Graphic file in python file  ")
lbel.grid()

entry = Entry(root, width = 10)
entry.grid(column=1, row = 2)

def clicked ():
    lbel.configure(text = " you clicked the Button")


button = Button(root , text = "Click me if you can ", fg = "red" ,command = clicked)
button .grid(column = 1 , row = 0)


menu = Menu(root)
item = Menu(menu)
item.add_command(label="New")
menu.add_cascade(label= "file",menu = item)
root.config(menu = menu)



root.mainloop()
