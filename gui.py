from tkinter import *

def action():
    print('Press OK!')

root = Tk()
root.geometry('1000x800')
root.title('Keypress statistic')
root.resizable(False, True)

panel1 = Frame(root)
panel1.place(width=500, relheight=1)

panel2 = Frame(root)
panel2.place(x= 500, width=500, relheight=1)


scrollbar = Scrollbar(panel1)
scrollbar.place(width=20, relheight=1)

text = Text(panel1)
text.insert(INSERT, "Hello.....\n")
text.place(in_=panel1, x=20, relwidth=1, relheight=1)
text.config(state=DISABLED)

scrollbar['command'] = text.yview
text['yscrollcommand'] = scrollbar.set

count = 0

def keypress(e):
    global count
    count+= 1
    text.config(state=NORMAL)
    text.insert(END, "{}. {} ({})\n".format(count, e.keycode, e.keysym))
    text.see(END)
    text.config(state=DISABLED)

root.bind('<KeyPress>', keypress)
root.mainloop()

