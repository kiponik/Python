class Stationary:
    def __init__(self):
        self.title = ''

    def draw(self):
        print('Запуст отрисовки')

class Pen(Stationary):
    def draw(self):
        print('Запуст отрисовки карандашом')

class Pencil(Stationary):
    def draw(self):
        print('Запуст отрисовки ручкой')

class Handle(Stationary):
    def draw(self):
        print('Запуст отрисовки кисточкой')

pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()