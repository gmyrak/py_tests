import random

MAX_KEY_LENGTH = 20


def plus1(L, k):
    M = list(L)
    M.append(k)
    return tuple(M)

def end_history(H, n):
    if n==0:
        return []
    else:
        return H[-n :]


def Predict(history):
    keys = set(history)  # Множество всех кнопок
    k = len(keys) # Количество кнопок
    history = history[-1000:]
    n = len(history)  # Длина всей последовательности
    stat_size = min(n, MAX_KEY_LENGTH)
    stat = {}

    for lkey in range(1, stat_size+1):
        stat[lkey] = {}
        for i in range(n-lkey+1):
            key = tuple( history[n-lkey - i : n-i] )
            stat[lkey][key]= stat[lkey].get(key, 0) + 1.001**(-i)

    key_result = {}

    for predict_level in range(1, stat_size+1):
        stat_level = stat[predict_level]
        for p in keys:
            key1 = plus1( end_history(history, predict_level-1), p )
            curr_val = stat_level.get(key1, 0)
            key_result[p] = key_result.get(p, 0) + curr_val*100**predict_level
            #key_result[p] = key_result.get(p, 0) + curr_val

    #print(key_result)

    super_best_key = None
    super_best_val = 0
    for k in key_result.keys():
        if key_result[k] > super_best_val:
            super_best_key = k
            super_best_val = key_result[k]

    return super_best_key

class Game:
    def __init__(self):
        'Начало новой игры'
        self.keys = set()  # Множество нажатых клавиш
        self.step = 1  # Шаг
        self.KeysCount = 0  # Коло-во клавиш в наборе
        self.predict = None  # Предсказание
        self.new = True  # Показывает, что нажата новая клавиша
        self.balans = 0  # Баланс игры
        self.mod_delta = 0
        self.history = []  # Вся последовательность нажатий
        self.stat = []
        self.tryes = 0
        self.oks = 0
        self.fails = 0


        print('Start Game!')

    def AcceptKey(self, code):
        '''Поступил новый символ'''
        if not code in self.keys:  # если символа не было в наборе
            self.keys.add(code)  # добавить в набор
            self.new = True  # показать, что был новый символ
            self.KeysCount += 1  # Увеличить количество
        else:
            self.new = False

        #if not self.new:  # только если символ уже был,
            # иначе не считается
            # (не трогаем баланс)
        #if self.predict:
        self.tryes+= 1
        if code == self.predict:  # Предсказание сбылось
            self.mod_delta = self.KeysCount - 1
            self.balans += self.KeysCount - 1  # Выигрыш
            self.oks+= 1
        else:
            self.mod_delta = 1
            self.balans -= 1  # проигрыш
            self.fails+= 1

        self.history.append(code)  # Добавляем символ в историю




        #self.predict = tuple(self.keys)[random.randint(0, len(self.keys)-1)]
        #self.predict = random.choice(tuple(self.keys))
        self.predict = Predict(self.history)
        self.step += 1
