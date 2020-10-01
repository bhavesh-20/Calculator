from tkinter import *
from functools import partial
root = Tk()
root.title("Calculator")
expression=StringVar()

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
    expression=entry_field.get()
    try:
        result=eval(expression)
        expression=str(result)
    except:
        expression="ERROR"
    display.set(expression)
    expression=""

expression=""
display = StringVar()
display.set(expression)

#row 1

ac = Button(root, text="AC", command=clear)
div = Button(root, text="/", command=partial(general_click,"/"))
mul = Button(root, text="*", command=partial(general_click,"*"))
sub = Button(root, text="-", command=partial(general_click,"-"))

#row 2

seven = Button(root, text="7", command=partial(general_click,"7"))
eight = Button(root, text="8", command=partial(general_click,"8"))
nine = Button(root, text="9", command=partial(general_click,"9"))
add = Button(root, text="+", command=partial(general_click,"+"))

#row 3
four = Button(root,text="4",command=partial(general_click,"4"))
five = Button(root,text="5",command=partial(general_click,"5"))
six = Button(root,text="6",command=partial(general_click,"6"))

#row 4

one = Button(root, text="1", command=partial(general_click,"1"))
two = Button(root, text="2", command=partial(general_click,"2"))
three = Button(root, text="3", command=partial(general_click,"3"))

#row 5

zero = Button(root, text="0", command=partial(general_click,"0"))
dot = Button(root, text=".", command=partial(general_click,"."))
equ = Button(root, text="=", command=equalto)

entry_field = Entry(root,textvariable=display,width=10,bd=0)

entry_field.grid(column=1,row=0)
ac.grid(column=0,row=0)
div.grid(column=0,row=1)
mul.grid(column=1,row=1)
sub.grid(column=2,row=1)
add.grid(column=3,row=1)
seven.grid(column=0,row=2)
eight.grid(column=1,row=2)
nine.grid(column=2,row=2)
four.grid(column=0,row=3)
five.grid(column=1,row=3)
six.grid(column=2,row=3)
one.grid(column=0,row=4)
two.grid(column=1,row=4)
three.grid(column=2,row=4)
zero.grid(column=0,row=5)
dot.grid(column=1,row=5)
equ.grid(column=2,row=5)

root = mainloop()


