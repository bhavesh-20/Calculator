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

#row 3

four = Button(root,text="4",command=general_click("4"))
five = Button(root,text="5",command=general_click("5"))
six = Button(root,text="6",command=general_click("6"))

root = mainloop()


