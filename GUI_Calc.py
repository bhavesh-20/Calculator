from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("CALCULATOR TEST")

        self.label = Label(master, text="CALCULATOR")

        self.first = Button(master, text="click here",fg="white",bg="black",command=self.thanks)

        self.second = Button(master, text="Exit", command=master.quit)
   
        self.third = Entry(master,width=20)

        self.fourth = ttk.Combobox(master)
        a=[int(x) for x in range(1,101)]
        a=tuple(a)
        self.fourth['values'] = a

        self.fifth = Checkbutton(master,text="Check",var=BooleanVar())

        self.sixth = scrolledtext.ScrolledText(master, width =10, height=1)
        




        self.label.grid(column=0,row=0)
        self.first.grid(column=1,row=1)
        self.second.grid(column=2,row=2)
        self.third.grid(column=3,row=3)
        self.fourth.grid(column=4,row=4)
        self.fifth.grid(column=5,row=5)
        self.sixth.grid(column=6,row=6)


        
    def thanks(self):
        self.label.configure(text="thanks "+self.third.get())
        self.sixth.insert(INSERT,self.third.get())
        messagebox.showinfo('Calculator',"ERROR!!!!!!!")
root=Tk()
gui = GUI(root)
root.mainloop()