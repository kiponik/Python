from abc import ABC, abstractmethod

class Coat:
    def __init__(self, size):
        self.consume = size / 6.5 + 0.5


class Costume:
    def __init__(self, height):
        self.consume = 2 * height + 0.3


class Clothes:
    def __init__(self):
        self.name = []
        self.final_consumation = []

    def coat_calculation(self, name, size):
        self.name.append(name)
        self.final_consumation.append(Coat(size))

    def costume_calculation(self, name, height):
        self.name.append(name)
        self.final_consumation.append(Costume(height))

    @property
    def final_calculation(self):
        final_result = 0
        for el in self.final_consumation:
            final_result += el.consume
        return final_result


item1 = Clothes()
item1.coat_calculation('Prada', 150)
item1.costume_calculation('Gucci', 200)
print(item1.name)
print(int(item1.final_calculation))