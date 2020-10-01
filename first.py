from tkinter import *
from functools import partial
root = Tk()
root.title("Calculator")
root.geometry("300x300")
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
display = StringVar()
display.set(expression)

frame = Frame(root,highlightbackground="Black",width=300,height=50,highlightcolor="Black")
frame.pack()
entry_field = Entry(frame,textvariable=display,width=300,bd=0,bg="Grey",fg="White",font=("arial",18,"bold"))

#row 0

bottom_frame = Frame(root,highlightbackground="Black",width=300,height=250,highlightcolor="Black")
ac = Button(bottom_frame, text="AC", command=clear,bg="White",fg="Black",height=2,width=42)
bottom_frame.pack()

#row 1

bottom_frame = Frame(root,highlightbackground="Black",width=300,height=250,highlightcolor="Black")
div = Button(bottom_frame, text="/", command=partial(general_click,"/"),bg="White",fg="Black",height=2,width=10)
mul = Button(bottom_frame, text="*", command=partial(general_click,"*"),bg="White",fg="Black",height=2,width=10)
sub = Button(bottom_frame, text="-", command=partial(general_click,"-"),bg="White",fg="Black",height=2,width=10)
add = Button(bottom_frame, text="+", command=partial(general_click,"+"),bg="White",fg="Black",height=2,width=10)
bottom_frame.pack()

#row 2

bottom_frame = Frame(root,highlightbackground="Black",width=300,height=250,highlightcolor="Black")
seven = Button(bottom_frame, text="7", command=partial(general_click,"7"),bg="White",fg="Black",height=2,width=14)
eight = Button(bottom_frame, text="8", command=partial(general_click,"8"),bg="White",fg="Black",height=2,width=14)
nine = Button(bottom_frame, text="9", command=partial(general_click,"9"),bg="White",fg="Black",height=2,width=14)
bottom_frame.pack()

#row 3

bottom_frame = Frame(root,highlightbackground="Black",width=300,height=250,highlightcolor="Black")
four = Button(bottom_frame,text="4",command=partial(general_click,"4"),bg="White",fg="Black",height=2,width=14)
five = Button(bottom_frame,text="5",command=partial(general_click,"5"),bg="White",fg="Black",height=2,width=14)
six = Button(bottom_frame,text="6",command=partial(general_click,"6"),bg="White",fg="Black",height=2,width=14)
bottom_frame.pack()

#row 4

bottom_frame = Frame(root,highlightbackground="Black",width=300,height=250,highlightcolor="Black")
one = Button(bottom_frame, text="1", command=partial(general_click,"1"),bg="White",fg="Black",height=2,width=14)
two = Button(bottom_frame, text="2", command=partial(general_click,"2"),bg="White",fg="Black",height=2,width=14)
three = Button(bottom_frame, text="3", command=partial(general_click,"3"),bg="White",fg="Black",height=2,width=14)
bottom_frame.pack()

#row 5

bottom_frame = Frame(root,highlightbackground="Black",width=300,height=250,highlightcolor="Black")
zero = Button(bottom_frame, text="0", command=partial(general_click,"0"),bg="White",fg="Black",height=2,width=14)
dot = Button(bottom_frame, text=".", command=partial(general_click,"."),bg="White",fg="Black",height=2,width=14)
equ = Button(bottom_frame, text="=", command=equalto,bg="White",fg="Black",height=2,width=14)
bottom_frame.pack()

entry_field.pack(ipady=10)
ac.pack(side=LEFT)
div.pack(side=LEFT)
mul.pack(side=LEFT)
sub.pack(side=LEFT)
add.pack(side=LEFT)
seven.pack(side=LEFT)
eight.pack(side=LEFT)
nine.pack(side=LEFT)
four.pack(side=LEFT)
five.pack(side=LEFT)
six.pack(side=LEFT)
one.pack(side=LEFT)
two.pack(side=LEFT)
three.pack(side=LEFT)
zero.pack(side=LEFT)
dot.pack(side=LEFT)
equ.pack(side=LEFT)

root = mainloop()


