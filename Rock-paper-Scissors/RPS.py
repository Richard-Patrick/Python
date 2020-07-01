import tkinter as tk
import tkinter.font as font
from tkinter import *
import random
import tkinter.messagebox

count=0
comp1=0
user1=0

def fre():
    global count,comp1,user1
    count = 0
    comp1 = 0
    user1 = 0
def rad(user):
    global count,comp1,user1
    com=random.choice(["Rock","Paper","Scissors","Rock","Paper","Scissors","Rock","Paper","Scissors"])
    config(com)
    condition(user,com)

def config(com):
    if com=="Rock":
        ans.configure(image=IR)
    elif com=="Paper":
        ans.configure(image=IP)
    elif com=="Scissors":
        ans.configure(image=IS)


def condition(user,com):
    global count, comp1, user1
    if count==4:
        if comp1>user1:
            yes=tkinter.messagebox.askquestion('Computer Wins',"Do you want to continue")
            if yes=='yes':
                fre()
            else:
                exit()
        else:
            yes = tkinter.messagebox.askquestion('Player Win',"Do you want to continue")
            if yes == "yes":
                fre()
            else:
                exit()
    else:
        if user==com:
            comp_text.set("Tie")
        elif user == "Rock":
            if com == "Paper":
                comp_text.set("computer Win")
                comp1+=1
                count+=1
            else:
                comp_text.set("Player Win")
                user1+=1
                count+= 1
        elif user == "Paper":
            if com=="Scissors":
                comp_text.set("computer Win")
                comp1+= 1
                count+= 1
            else:
                comp_text.set("Player Win")
                user1+= 1
                count+= 1
        elif user == "Scissors":
            if com=="Rock":
                comp_text.set("computer Win")
                comp1+= 1
                count+= 1
            else:
                comp_text.set("Player Win")
                user1+= 1
                count+= 1


win=Tk()
win.title("Rock–paper–scissors".center(200))

uf=Frame(win)


IR = tk.PhotoImage(file="R.png")
IP = tk.PhotoImage(file="P.png")
IS = tk.PhotoImage(file="S.png")
IRSP = tk.PhotoImage(file="RPS.png")
comp_text=tk.StringVar()



uf.pack(side=TOP)
Rb=Button(uf, compound=tk.TOP, width=250, height=416, image=IR,command= lambda :rad("Rock"))
Rb.pack(side=LEFT)
Pb=Button(uf, compound=tk.TOP, width=250, height=416, image=IP,command= lambda :rad("Paper"))
Pb.pack(side=LEFT)
Sb=Button(uf, compound=tk.TOP, width=250, height=416, image=IS,command= lambda :rad("Scissors"))
Sb.pack(side=LEFT)

ins=Button(uf,textvariable=comp_text ,compound=tk.TOP, width=10, height=5)
ins.pack(side=LEFT)

comp_text.set("Play")

ans=Button(uf, compound=tk.TOP, width=250, height=416, image=IRSP)
ans.pack(side=LEFT)


win.mainloop()