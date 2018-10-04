from tkinter import *
from  GameLogic import *

game = Game()

Window = Tk()
Window.geometry('1000x500+20+20')
Window.title('Статистика нажатий клавиш')

Window.resizable(False, True)

Panel1 = Frame(Window)
Panel1.place(width=500, relheight=1)

Panel2 = Frame(Window)
Panel2.place(x= 500, width=500, relheight=1)

text = Text(Panel1)
text.insert(INSERT, "Hello.....\n")
text.place(x=20, relwidth=1, relheight=1)
text.config(state=DISABLED)

Scrol = Scrollbar(Panel1)
Scrol.place(width=20, relheight=1)

Scrol['command'] = text.yview
text['yscrollcommand'] = Scrol.set

def restart():
    global game
    game = Game()

Lab1 = Label(Panel2, text='0')
Lab1.place(x=150, y=20)

ButtonRestart = Button(Panel2, text='New Game', command=restart)
ButtonRestart.place(x=10, y=20, width=80, height=30)

ButtonActivate = Button(Panel2, text='Activate', command= lambda :game.enable())
ButtonActivate.place(x=10, y=60, width=80, height=30)

def keypress(e):
    if game.active:
        game.step()
        text.config(state=NORMAL)
        text.insert(END, "{}.\t{}\t({}) {}\n".format(game.steps, e.keycode, e.keysym, game.newcode(e.keycode)))
        Lab1.configure(text= len(game.keys))
        text.see(END)
        text.config(state=DISABLED)

Window.bind('<KeyPress>', keypress)

Window.mainloop()