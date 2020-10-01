from tkinter import *

root = Tk()
display = Entry(root, width=10)

#row 1

ac = Button(root, text="AC", clear())
div = Button(root, text="/", general_click("/"))
mul = Button(root, text="*", general_click("*"))
sub = Button(root, text="-", general_click("-"))

#row 2


root = mainloop()