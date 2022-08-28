from tkinter import *
  
root = Tk()
#above create a  Main window or Widget named as root 

#  Now frame name Frame  class is inherited by root 
frame = Frame(root)
frame.pack()
# Creating the button on frame 
redbutton = Button(frame, text = 'Red', fg ='red')
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text = 'Brown', fg='brown')
greenbutton.pack( side = LEFT )
bluebutton = Button(frame, text ='Blue', fg ='blue')
bluebutton.pack( side = LEFT )

# Creating another child of root as button 
buttomframe=Frame(root)
buttomframe.pack(side= BOTTOM)


blackbutton = Button(buttomframe, text ='Black', fg ='black')
blackbutton.pack( side = BOTTOM)

middlebutton= Button(buttomframe,  label = "top",activebackground="red" ,fg = "yellow").pack(side = TOP)

root.mainloop()