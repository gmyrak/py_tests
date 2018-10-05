from tkinter import *
#from PIL import ImageTk, Image
# hellll dev 4

sizeX = 500
sizeY = 400

root = Tk()
root.resizable(False, False) # запретить изменять размер вручную
# root.geometry('800x600+20+20')


canvas = Canvas(root, width=sizeX, height=sizeY, cursor='pirate', bg='green')
# cursor:
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/cursors.html
canvas.pack()

# Полный экран
#root.attributes('-fullscreen', True)


canvas.bell()
# Разрешение экрана
screenX = root.winfo_screenwidth()
screeY = root.winfo_screenheight()

canvas.configure(cursor='circle', bg='black') # изменить параметры канвы
# или canvas.config


canvas.create_line([20, 10], [400, 100], [300, 20], arrow=BOTH, fill='red', width=3, tags='group1')
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/create_line.html


canvas.create_rectangle([100, 100], [200, 300], tags='group1', fill='red')
canvas.create_rectangle([110, 110], [220, 320], tags='group1', fill=None)

#pilImage = Image.open("d:/1/pic1.png")
p1 = PhotoImage(file="PNG_transparency_demonstration_1.png")
p2 = PhotoImage(file="tumblr_ob3djdTZO71vzbuubo1_400.png")

im = canvas.create_image(250, 200, image=p2)


def kp(e):
    print(e)
    canvas.itemconfigure(im, image=p1)

root.bind('<KeyPress>', lambda e: canvas.itemconfig(im, image=p1) if e.keysym=='space' else '')


root.mainloop()