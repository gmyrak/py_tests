class Game:

    def __init__(self):
        'Начало новой игры'
        self.keys = set()
        self.steps = 0
        self.count = 0
        self.active = False
        print('Start Game!')

    def enable(self):
        self.active = True

    def disable(self):
        self.active = False

    def newcode(self, kode):
        if kode in self.keys:
            return False
        else:
            self.keys.add(kode)
            self.count+=1
            return True

    def step(self):
        self.steps+=1