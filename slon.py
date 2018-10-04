from re import *

Согласие = compile(r'(\bда\b|\w*куп\w*|\bOK\b)', IGNORECASE)
Торг = compile(r'(\d+)')
Тигр = compile(r'\bтигр', IGNORECASE)

Цена = 0
print('- Купи слона')

while True:
    Цена+= 100
    Ответ = input('- ')

    res = search(Тигр, Ответ)
    if res:
        print('У нас нет тигров. Купите слона')
        continue

    res = search(Торг, Ответ)
    if res:
        Предложение = int(res.group(1))
        if Предложение >= Цена:
            print('Достойное предложение. Вы купили слона за {}$'.format(Предложение))
            break
        else:
            print('{}$ этого мало. Надо больше'.format(Предложение))
            continue

    res = search(Согласие, Ответ)
    if res:
        print('Вы сказали "{}". Куплено'.format(res.group(1)))
        print('Слон выслан. С вас {}$'.format(Цена))
        break

    if Ответ=='':
        print('Чего молчишь? Купи слона')
        continue

    print('- Все говорят "{0}", a ты купи слона'.format(Ответ) )

