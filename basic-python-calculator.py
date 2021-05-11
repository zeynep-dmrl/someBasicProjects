from tkinter import *
import parser
from math import factorial

root = Tk()
#root.geometry('270x320')
#root.minsize(width=200, height=200)
root.config(bg ='black')
root.title('Calculator')

i=0
def get_variables(num):
    global i
    display.insert(i,num)
    i += 1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i += length

def clearAll():
    display.delete(0,END)

def undo():
    #son elemanı siler
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clearAll()
        display.insert(0,new_string)
    else:
        clearAll()
        display.insert(0,"Error")

def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clearAll()
        display.insert(0,result)
    except Exception:
        clearAll()
        display.insert(0,"Error")

def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clearAll()
        display.insert(0,result)
    except Exception:
        clearAll()
        display.insert(0,"Error")    


#---------------------DESIGN-----------------------


display = Entry(root,width=45)
display.grid(row=1, columnspan= 6,sticky=NSEW)

Button(root,text="1",command = lambda:get_variables(1),bg="white",width=5,height=3,font="bold").grid(row=2,column=0,sticky=NSEW)
Button(root,text="2",command = lambda:get_variables(2),bg="white",width=5,height=3,font="bold").grid(row=2,column=1,sticky=NSEW)
Button(root,text="3",command = lambda:get_variables(3),bg="white",width=5,height=3,font="bold").grid(row=2,column=2,sticky=NSEW)

Button(root,text="4",command = lambda:get_variables(4),bg="white",width=5,height=3,font="bold").grid(row=3,column=0,sticky=NSEW)
Button(root,text="5",command = lambda:get_variables(5),bg="white",width=5,height=3,font="bold").grid(row=3,column=1,sticky=NSEW)
Button(root,text="6",command = lambda:get_variables(6),bg="white",width=5,height=3,font="bold").grid(row=3,column=2,sticky=NSEW)

Button(root,text="7",command = lambda:get_variables(7),bg="white",width=5,height=3,font="bold").grid(row=4,column=0,sticky=NSEW)
Button(root,text="8",command = lambda:get_variables(8),bg="white",width=5,height=3,font="bold").grid(row=4,column=1,sticky=NSEW)
Button(root,text="9",command = lambda:get_variables(9),bg="white",width=5,height=3,font="bold").grid(row=4,column=2,sticky=NSEW)

Button(root,text="C",command = lambda:clearAll(),fg="red",width=5,height=3).grid(row=5,column=0,sticky=NSEW)
Button(root,text="0",command = lambda:get_variables(0),bg="white",width=5,height=3,font="bold").grid(row=5,column=1,sticky=NSEW)
Button(root,text=" .",command = lambda:get_variables("."),width=5,height=3).grid(row=5,column=2,sticky=NSEW)

Button(root,text="+",command = lambda:get_operation("+"),width=7,height=3).grid(row=2,column=3,sticky=NSEW)
Button(root,text="-",command = lambda:get_operation("-"),width=7,height=3).grid(row=3,column=3,sticky=NSEW)
Button(root,text="*",command = lambda:get_operation("*"),width=7,height=3).grid(row=4,column=3,sticky=NSEW)
Button(root,text="/",command = lambda:get_operation("/"),width=7,height=3).grid(row=5,column=3,sticky=NSEW)

Button(root,text="pi",command = lambda:get_operation("*3.14"),width=7,height=3).grid(row=2,column=4,sticky=NSEW)
Button(root,text="%",command = lambda:get_operation("%"),width=7,height=3).grid(row=3,column=4,sticky=NSEW)
Button(root,text="(",command = lambda:get_operation("("),width=7,height=3).grid(row=4,column=4,sticky=NSEW)
Button(root,text="exp",command = lambda:get_operation("**"),width=7,height=3).grid(row=5,column=4,sticky=NSEW)

Button(root,text="<-",command = lambda:undo(),width=7,height=3).grid(row=2,column=5,sticky=NSEW)
Button(root,text="x!",command = lambda:fact(),width=7,height=3).grid(row=3,column=5,sticky=NSEW)
Button(root,text=")",command = lambda:get_operation(")"),width=7,height=3).grid(row=4,column=5,sticky=NSEW)
Button(root,text="^2",command = lambda:get_operation("**2"),width=7,height=3).grid(row=5,column=5,sticky=NSEW)

Button(root,text="=",command = lambda:calculate(),fg = "blue",height=5).grid(columnspan=6,sticky=EW)

root.mainloop()
#sticky=NSEW