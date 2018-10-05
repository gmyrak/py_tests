from random import *
from tkinter import *

circlies = 400
sizeX = 600
sizeY = 600
R = 100
vmax = 5
interval = 10

'dev 3'

root = Tk()
#root.wm_attributes(fullscreen=True)
#root.geometry('+20+20')
#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
#root.wm_maxsize()

root.attributes('-fullscreen', True)

#root.overrideredirect(1) # убираем заголовок окна
#root.state('zoomed')

#root.resizable(False, False)
#root.state('zoomed')

sizeX = root.winfo_screenwidth()
sizeY = root.winfo_screenheight()



canvas = Canvas(root, width=sizeX, height=sizeY)
canvas.pack()

print(root.winfo_screenwidth(), root.winfo_screenheight())

circles = {}

for i in range(circlies):
    colors = choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange',
                     'pink', 'purple', 'red','yellow', 'violet', 'indigo',
                     'chartreuse', 'lime', '#f55c4b' ])

    r =  randint(1, R)
    x0 = randint(0, sizeX)
    y0 = randint(0, sizeY)

    c = canvas.create_oval(x0-r, y0-r, x0+r, y0+r, fill=colors)
    circles[c] = {'vx': randint(-vmax, vmax), 'vy': randint(-vmax, vmax)}
    #canvas.update()


def move_circles():
    for id in circles:

        item = circles[id]

        x1, y1, x2, y2 = canvas.coords(id)
        if x1<0: item['vx'] = abs(item['vx'])
        if y1<0: item['vy'] = abs(item['vy'])
        if x2>sizeX: item['vx'] = -abs(item['vx'])
        if y2>sizeY: item['vy'] = -abs(item['vy'])

        canvas.move(id, item['vx'], item['vy'])

    canvas.after(interval, move_circles)

def Action(e):
    print(e.x, e.y)
    over = canvas.find_overlapping(e.x, e.y, e.x, e.y)
    for id in over:
        #canvas.itemconfigure(id, state='hidden')
        #circles[id] = {'vx': randint(-vmax, vmax), 'vy': randint(-vmax, vmax)}
        canvas.delete(id)
        circles.pop(id)


canvas.bind('<Button-1>', Action)

move_circles()
root.mainloop()