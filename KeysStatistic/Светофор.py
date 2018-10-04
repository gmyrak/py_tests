from tkinter import *

R = 50
h = 30

root = Tk()
root.title('Светофор')
root.resizable(False, False)

canvas = Canvas(root, width=2*R+2*h, height=6*R+4*h)
canvas.pack()

red    = canvas.create_oval(h, h,        h+2*R,  h+2*R)
yellow = canvas.create_oval(h, 2*h+2*R,  h+2*R,  2*h+4*R)
green  = canvas.create_oval(h, 3*h+4*R,  h+2*R,  3*h+6*R)

def set_mode(mode):
    if mode == 0:  # off
        canvas.itemconfigure(red, fill='gray')
        canvas.itemconfigure(yellow, fill='gray')
        canvas.itemconfigure(green, fill='gray')
    elif mode == 1:  # red
        canvas.itemconfigure(red, fill='red')
        canvas.itemconfigure(yellow, fill='gray')
        canvas.itemconfigure(green, fill='gray')
        return 2, 3000
    elif mode == 2:  # red + yellow
        canvas.itemconfigure(red, fill='red')
        canvas.itemconfigure(yellow, fill='yellow')
        canvas.itemconfigure(green, fill='gray')
        return 3, 1000
    elif mode == 3:  # green
        canvas.itemconfigure(red, fill='gray')
        canvas.itemconfigure(yellow, fill='gray')
        canvas.itemconfigure(green, fill='green')
        return 4, 3000
    elif mode == 4:  # yellow
        canvas.itemconfigure(red, fill='gray')
        canvas.itemconfigure(yellow, fill='yellow')
        canvas.itemconfigure(green, fill='gray')
        return 1, 1000


def run():
    global work, curr_mode, run_id
    if work:
        curr_mode, time = set_mode(curr_mode)
        run_id = canvas.after(time, run)


def switch():
    global work, curr_mode, run_id
    if work:
        work = False
        But.configure(text='Светофор выключен')
        canvas.after_cancel(run_id)
        set_mode(0)
    else:
        work = True
        But.configure(text='Светофор работает')
        curr_mode = 1
        run()

But = Button(root, command=switch)
But.pack()

work = False
switch()
root.mainloop()