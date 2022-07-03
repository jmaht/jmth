import sys
from tkinter import *
from tkinter import ttk
import random
allloses=0
allwins=0
def scr():
    global allloses
    global allwins
    wins = 0
    allloses=0
    allwins=0
    win = Tk()
    win.geometry("1920x1080")
    win.title("rpc")
    computer_options = {
        "0": "Камень",
        "1": "Бумага",
        "2": "Ножницы"
    }
    def exits():
        if allloses==3:
            return 1
            scr.exit()
        if allwins==3:
            return -1
            win.destroy()
    def isrock():
        global wins
        global allwins
        global allloses
        value = computer_options[str(random.randint(0, 2))]
        if random.randint(0, 2) == 2:
            value = "Бумага"
            match_result = "Комп выиграл"
            allloses += 1
        elif value == "Камень":
            match_result = "Ничья"
        elif value == "Ножницы":
            allwins += 1
            match_result = "UwU ты win"
        else:
            match_result = "Комп выиграл"
            allloses += 1
        if allwins == 3 or allloses == 3:
            scr.exits()
        label.config(text=match_result)
        l1.config(text="Камень")
        l3.config(text=value)

    def ispaper():
        global wins
        global allloses
        global allwins
        value = computer_options[str(random.randint(0, 2))]
        if random.randint(0, 2) == 1:
            value = "Ножницы"
            match_result = "Комп выиграл"
            allloses+=1
        elif value == "Бумага":
            match_result = "Ничья"
        elif value == "Ножницы":
            match_result = "Комп выиграл"
            allloses += 1
        else:
            match_result = "Ты выиграл"
            allwins += 1
        if allwins == 3 or allloses == 3:
            scr.exits()
        label.config(text=match_result)
        l1.config(text="Бумага")
        l3.config(text=value)

    def isscissor():
        global wins
        global allwins
        global allloses
        value = computer_options[str(random.randint(0, 2))]
        if random.randint(0, 2) == 1:
            value = "Камень"
            match_result = "Комп выиграл"
            allloses += 1
        if value == "Камень":
            match_result = "Бот Выиграл"
            allloses += 1
        elif value == "Ножницы":
            match_result = "Ничья"
        else:
            match_result = "Ты выиграл"
            allwins += 1
        if allwins == 3 or allloses == 3:
            exits()
        label.config(text=match_result)
        l1.config(text="Ножницы")
        l3.config(text=value)

    # Create a LabelFrame
    labelframe = LabelFrame(win, text="Камень Ножницы Бумага", font=('Century 20 bold'), labelanchor="n", bd=5,
                            bg="khaki3", width=1920, height=1080, cursor="target")
    labelframe.pack(expand=True, fill=BOTH)
    l1 = Label(labelframe, text="Игрок", font=('Helvetica 18 bold'))
    l1.place(relx=.18, rely=.1)
    l2 = Label(labelframe, text="VS", font=('Helvetica 18 bold'), bg="khaki3")
    l2.place(relx=.45, rely=.1)
    l3 = Label(labelframe, text="Компьютер", font=('Helvetica 18 bold'))
    l3.place(relx=.65, rely=.1)
    label = Label(labelframe, text="", font=('Coveat', 25, 'bold'), bg="khaki3")
    label.pack(pady=150)
    b1 = Button(labelframe, text="Камень", font=10, width=7, command=isrock)
    b1.place(relx=.25, rely=.62)
    b2 = Button(labelframe, text="Бумага", font=10, width=7, command=ispaper)
    b2.place(relx=.41, rely=.62)
    b3 = Button(labelframe, text="Ножницы", font=10, width=7, command=isscissor)
    b3.place(relx=.58, rely=.62)
    b4 = Button(labelframe, text="Exit", font=10, width=7, command=exits)
    b4.place(relx=.95, rely=.95)
    win.mainloop()
scr()



