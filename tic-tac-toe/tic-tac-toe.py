from tkinter import *
import random
import tkinter.messagebox

buttons=[]
click = True
tk = None
count=0

def start():
    global tk,buttons,count
    count=0
    tk = Tk()
    tk.title("Tic Tac Toe")
    def play(button):
        global click, tk,count
        click=True
# ----------------------------------player and computer-------------------------------------------------------
        if button["text"] == " ":
            button["text"] = "X"
            count = count + 1     
            while click:
                if count == 1:
                    if button5["text"] == " ":
                        button5['text'] = "O"
                    else:
                        button3['text'] = "O"
                    click = FALSE
                    count = count + 1
                elif count != 8:
                    button = buttons[random.randint(0, 8)]
                    if button["text"] == " ":
                        button['text'] = "O"
                        click = FALSE
                        count = count + 1
                else:
                    click = FALSE
                    count = count + 1
#-------------------------------condiction--------------------------------------------------------------------
        if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
            button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
            button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
            button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
            button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
            button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
            answer = tkinter.messagebox.askquestion('X Player wins!!!', 'Do you want to play again')
            tk.destroy()
            if answer == 'yes': start()
        elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
            button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
            button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
            button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
            button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
            button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
            button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
            button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
            answer = tkinter.messagebox.askquestion('O Player wins!!!', 'Do you want to play again')
            tk.destroy()
            if answer == 'yes': start()
        elif count == 9:
            answer = tkinter.messagebox.askquestion('Game Tie!!!', 'Do you want to play again')
            tk.destroy()
            if answer == 'yes': start()

# -------------------------------buttons-------------------------------------------------------------------
    buttonstyle="Arial 25 bold"
    
    button1 = Button(tk, text=" ", font=(buttonstyle), height=4, width=8, command=lambda:play(button1))
    button1.grid(row=1, column=0, sticky=S+N+E+W)

    button2 = Button(tk, text=" ", font=(buttonstyle), height=4, width=8, command=lambda:play(button2))
    button2.grid(row=1, column=1, sticky=S+N+E+W)

    button3 = Button(tk, text=" ", font=(buttonstyle), height=4, width=8, command=lambda:play(button3))
    button3.grid(row=1, column=2, sticky=S+N+E+W)

    button4 = Button(tk, text=" ", font=(buttonstyle), height=4, width=8, command=lambda:play(button4))
    button4.grid(row=2, column=0, sticky=S+N+E+W)

    button5 = Button(tk, text=" ", font=(buttonstyle), height=4, width=8, command=lambda:play(button5))
    button5.grid(row=2, column=1, sticky=S+N+E+W)

    button6 = Button(tk, text=" ", font=(buttonstyle), height=4, width=8, command=lambda:play(button6))
    button6.grid(row=2, column=2, sticky=S+N+E+W)

    button7 = Button(tk, text=" ", font=(buttonstyle), height=4, width=8, command=lambda:play(button7))
    button7.grid(row=3, column=0, sticky=S+N+E+W)

    button8 = Button(tk, text=" ", font=(buttonstyle), height=4, width=8, command=lambda:play(button8))
    button8.grid(row=3, column=1, sticky=S+N+E+W)

    button9 = Button(tk, text=" ", font=(buttonstyle), height=4, width=8, command=lambda:play(button9))
    button9.grid(row=3, column=2, sticky=S+N+E+W)
    
    
    buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

    tk.mainloop()

start()