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

seven = Button(root, text="7", command=general_click("7"))
eight = Button(root, text="8", command=general_click("8"))
nine = Button(root, text="9", command=general_click("9"))
add = Button(root, text="+", command=general_click("+"))

#row 4

one = Button(root, text="1", command=general_click("1"))
two = Button(root, text="2", command=general_click("2"))
three = Button(root, text="3", command=general_click("3"))

#row 5

zero = Button(root, text="0", command=general_click("0"))
dot = Button(root, text=".", command=general_click("."))
equ = Button(root, text="=", command=general_click("="))


root = mainloop()


