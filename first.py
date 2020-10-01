import tkinter

expression=tkinter.Stringvar()

def general_click(item):
    expression=expression+item
    display.set(expression)

def clear():
    expression=""
    display.set(expression)

def equalto():
    result=eval(expression)
    expression=str(result)
    display.set(expression)
