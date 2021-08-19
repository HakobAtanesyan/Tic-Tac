from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic tac game with python")

clicked = True
count = 0


def disable_all_buttons():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)

    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)

    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)

def chek_if_von():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo('Tic tac', "x-ը հաղթեց, ՇՆՈՐՀԱՎՈՐ")
        disable_all_buttons()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo('Tic tac', "x-ը հաղթեց, ՇՆՈՐՀԱՎՈՐ")
        disable_all_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo('Tic tac', "x-ը հաղթեց, ՇՆՈՐՀԱՎՈՐ")
        disable_all_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo('Tic tac', "x-ը հաղթեց, ՇՆՈՐՀԱՎՈՐ")
        disable_all_buttons()

    elif b2["text"] == "X" and b5["text"] == "x" and b8["text"] == "x":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo('Tic tac', "x-ը հաղթեց, ՇՆՈՐՀԱՎՈՐ")
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo('Tic tac', "x-ը հաղթեց, ՇՆՈՐՀԱՎՈՐ")
        disable_all_buttons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo('Tic tac', "x-ը հաղթեց, ՇՆՈՐՀԱՎՈՐ")
        disable_all_buttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo('Tic tac', "x-ը հաղթեց, ՇՆՈՐՀԱՎՈՐ")
        disable_all_buttons()

    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo('Tic tac', "O-ն հաղթեց, ՇՆՈՐՀԱՎՈՐ")
        disable_all_buttons()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo('Tic tac', "O-ն հաղթեց, ՇՆՈՐՀԱՎՈՐ")
        disable_all_buttons()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo('Tic tac', "O-ն հաղթեց, ՇՆՈՐՀԱՎՈՐ")
        disable_all_buttons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo('Tic tac', "O-ն հաղթեց, ՇՆՈՐՀԱՎՈՐ")
        disable_all_buttons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo('Tic tac', "O-ն հաղթեց, ՇՆՈՐՀԱՎՈՐ")
        disable_all_buttons()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo('Tic tac', "O-ն հաղթեց, ՇՆՈՐՀԱՎՈՐ")
        disable_all_buttons()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo('Tic tac', "O-ն հաղթեց, ՇՆՈՐՀԱՎՈՐ")
        disable_all_buttons()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo('Tic tac', "O-ն հաղթեց, ՇՆՈՐՀԱՎՈՐ")
        disable_all_buttons()


def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        chek_if_von()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        chek_if_von()
    else:
        messagebox.showerror('Tic tac', "Այդ տարբերակը արդեն սեղմված է  \n ընտրեք այլ տարբերակ")


b1 = Button(text=" ", font=("Arial)", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: b_click(b1))
b1.grid(row=0, column=0)
b2 = Button(text=" ", font=("Arial)", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: b_click(b2))
b2.grid(row=1, column=0)
b3 = Button(text=" ", font=("Arial)", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: b_click(b3))
b3.grid(row=2, column=0)

b4 = Button(text=" ", font=("Arial)", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: b_click(b4))
b4.grid(row=0, column=1)
b5 = Button(text=" ", font=("Arial)", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: b_click(b5))
b5.grid(row=1, column=1)
b6 = Button(text=" ", font=("Arial)", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: b_click(b6))
b6.grid(row=2, column=1)

b7 = Button(text=" ", font=("Arial)", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: b_click(b7))
b7.grid(row=0, column=2)
b8 = Button(text=" ", font=("Arial)", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: b_click(b8))
b8.grid(row=1, column=2)
b9 = Button(text=" ", font=("Arial)", 20), height=2, width=5, bg="SystemButtonFace", command=lambda: b_click(b9))
b9.grid(row=2, column=2)

root.mainloop()
