from tkinter import *
from functools import partial
root = Tk()
root.title("Calculator")
root.geometry("300x300")
expression=StringVar()

frame = Frame(root,highlightbackground="Black",width=300,height=50,highlightcolor="Black")
frame.pack()

bottom_frame = Frame(root,highlightbackground="Black",width=300,height=50,highlightcolor="Black")
bottom_frame.pack()

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
display = StringVar()
display.set(expression)
entry_field = Entry(frame,textvariable=display,width=300,bd=0,bg="Grey",fg="White",font=("arial",18,"bold"))

#row 1

ac = Button(bottom_frame, text="AC", command=clear)
div = Button(bottom_frame, text="/", command=partial(general_click,"/"))
mul = Button(bottom_frame, text="*", command=partial(general_click,"*"))
sub = Button(bottom_frame, text="-", command=partial(general_click,"-"))

#row 2

seven = Button(bottom_frame, text="7", command=partial(general_click,"7"))
eight = Button(bottom_frame, text="8", command=partial(general_click,"8"))
nine = Button(bottom_frame, text="9", command=partial(general_click,"9"))
add = Button(bottom_frame, text="+", command=partial(general_click,"+"))

#row 3
four = Button(bottom_frame,text="4",command=partial(general_click,"4"))
five = Button(bottom_frame,text="5",command=partial(general_click,"5"))
six = Button(bottom_frame,text="6",command=partial(general_click,"6"))

#row 4

one = Button(bottom_frame, text="1", command=partial(general_click,"1"))
two = Button(bottom_frame, text="2", command=partial(general_click,"2"))
three = Button(bottom_frame, text="3", command=partial(general_click,"3"))

#row 5

zero = Button(bottom_frame, text="0", command=partial(general_click,"0"))
dot = Button(bottom_frame, text=".", command=partial(general_click,"."))
equ = Button(bottom_frame, text="=", command=equalto)


#entry_field.grid(column=0,row=0)
entry_field.pack(ipady=10)
"""
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
"""
ac.pack(side=RIGHT)


root = mainloop()


