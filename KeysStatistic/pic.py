import pickle
from tkinter import *


Window = Tk()
Window.geometry('800x600+20+20') # Ширина x Высота + Отступ справа + Отступ слева
Window.title('Коллекция клавиш') # заголовок окна
Window.resizable(False, False) # Можно изменять размер только по вертикали

def keypress(e):
    code = e.keycode
    sym = e.keysym
    print(code, sym)


Window.bind('<KeyPress>', keypress)
Window.mainloop()
