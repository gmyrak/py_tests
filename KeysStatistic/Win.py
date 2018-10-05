from tkinter import *
from  Game import *
'''Master'''
'''dev 3 p72 dev to contin...'''


edit_mode = False # Реагировать на клавиши
ShowPredict = True # Показывать предсказание
SYM = {}

# Определяем главное окно
Window = Tk()
Window.geometry('1000x600+20+20') # Ширина x Высота + Отступ справа + Отступ слева
Window.title('Статистика нажатий клавиш') # заголовок окна
Window.resizable(False, True) # Можно изменять размер только по вертикали

Panel1 = Frame(Window); Panel1.place(width=500, relheight=1) # Левая панель для текстового поля
Panel2 = Frame(Window); Panel2.place(x= 500, width=500, relheight=1) # Правая панель для информации и настроек

# Текстовое поле для вывода информации о ходе игры
text = Text(Panel1)
text.place(x=20, relwidth=1, relheight=1) # Левый край отступает 20px -
# это место для линейки прокрутки
# относительные ширина и высота =1
# это значит, что занимаем всё доступное место
# в родительском компоненте (Panel1)

text.config(state=DISABLED) # Запрещаем изменение текста вручную

text.tag_config('default', font='"Courier New" 14')
text.tag_config('ok',      font='"Courier New" 14 bold', foreground='green')
text.tag_config('fail',    font='"Courier New" 14 bold', foreground='red')

def write(msg, style='default'):
    '''Процедура для записи в текстовое поле
    Текст "только для чтения" - мы не можем писать туда вручную,
    только со стороны программы'''
    text.config(state=NORMAL) # Разрешаем изменение
    text.insert(END, msg, style) # Записываем сообщение в конец текста
    text.config(state=DISABLED) # Запрещаем изменение
    text.see(END) # Позииционируемся в конец

def CleanText():
    '''Процедура очистки текста'''
    text.config(state=NORMAL) # Разрешаем изменение
    text.delete('1.0', END) # удаляем от первой строки, нулевой позиции до самого конца
    text.config(state=DISABLED) # Запрещаем изменение

#write("Hello.....\n")

# Создаем линейку прокрутки и связываем её с текстовым полем
Scrol = Scrollbar(Panel1); Scrol.place(width=20, relheight=1)
Scrol['command'] = text.yview; text['yscrollcommand'] = Scrol.set

# Метка для вывода информации
LabelInfo = Label(Panel2, justify=LEFT, font='Verdana 16')
LabelInfo.place(x=10, y=150)

def UpdateInfo():
    if game.tryes==0:
        percent = '...'
    else:
        percent = round(100*game.oks/game.tryes, 2)

    if game.step == 1:
        ave = '...'
    else:
        ave = round(game.balans/(game.step-1), 4)

    LabelInfo.configure(text='Кнопок: {}\n'
                             'Нажатий: {}\n'
                             'Баланс: {}\n'.format(game.KeysCount, game.step-1, game.balans) +
                             'В среднем: {}\n'.format(ave) +
                             'Угадано: {}/{} = {}%'.format(game.oks, game.tryes, percent)

                        )
def NewGame():
    global game, edit_mode
    game = Game()
    edit_mode = True
    UpdateInfo()
    CleanText()
    Prompt()

ButtonRestart = Button(Panel2, text='New Game', command=NewGame)
ButtonRestart.place(x=10, y=20, width=80, height=30)

def LockUnlock():
    global edit_mode
    if edit_mode:
        edit_mode = False
        ButtonActivate.configure(text='Edit')
    else:
        edit_mode = True
        ButtonActivate.configure(text='Set')

ButtonActivate = Button(Panel2, text='Edit', command=LockUnlock)
ButtonActivate.place(x=10, y=60, width=80, height=30)

VarShowPredict = BooleanVar()

def SetShowPredict():
    global ShowPredict
    ShowPredict= VarShowPredict.get()

CheckShowPredict = Checkbutton(Panel2, text='Показывать предсказание', variable=VarShowPredict, command=SetShowPredict)
CheckShowPredict.place(x=10, y=100)
VarShowPredict.set(ShowPredict)

def Prompt():
    if ShowPredict:
        if game.predict:
            PredictToShow = '{} ({})'.format(game.predict, SYM[game.predict])
        else:
            PredictToShow = '...'
    else:
        PredictToShow = '?'
    write('{}. {} = '.format(game.step, PredictToShow))

def keypress(e):
    if edit_mode:
        Predict = game.predict
        code = e.keycode; sym = e.keysym
        SYM[code] = sym
        game.AcceptKey(code)

        if code==Predict:
            write("{0}({1})\t".format(code, sym))
            write("+{0}\n".format(game.mod_delta), 'ok')
        else:
            write("{0}({1})\t".format(code, sym))
            write("-{0}\n".format(game.mod_delta), 'fail')

        UpdateInfo()
        Prompt()

Window.bind('<KeyPress>', keypress)
NewGame()
Window.mainloop()