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

def set_light(r, g, y):
    canvas.itemconfigure(red, fill= 'red' if r else 'gray')
    canvas.itemconfigure(green, fill='green' if g else 'gray')
    canvas.itemconfigure(yellow, fill='yellow' if y else 'gray')


def set_mode(mode):
    if mode == 0:  # off
        set_light(0, 0, 0)
    elif mode == 1:  # red
        set_light(1, 0, 0)
        return 2, 3000
    elif mode == 2:  # red + yellow
        set_light(1, 0, 1)
        return 3, 1000
    elif mode == 3:  # green
        set_light(0, 1, 0)
        return 4, 3000
    elif mode == 4:  # yellow
        set_light(0, 0, 1)
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