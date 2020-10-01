from tkinter import *

root = Tk()

expression=""

def general_click(item):
    global expression
    expression=expression+item
    display.set(expression)

def clear():
    global expression
    expression=""
    display.set(expression)

def equalto():
    global expression
    result=eval(expression)
    expression=str(result)
    display.set(expression)


display = Entry(root, width=10)

#row 1

ac = Button(root, text="AC", command=clear())
div = Button(root, text="/", command=general_click("/"))
mul = Button(root, text="*", command=general_click("*"))
sub = Button(root, text="-", command=general_click("-"))

#row 2


root = mainloop()


