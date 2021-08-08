class Car:
    speed = ''
    color = ''
    name = ''
    is_police = False

    def __init__(self, parameter1, parameter2, parameter3, parameter4):
        Car.speed = parameter1
        Car.color = parameter2
        Car.name = parameter3
        Car.is_police = parameter4

    def go(self):
        return

    def stop(self):
        return

    def turn(self, direction):
        return

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            print('Скорость превышена')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            print('Скорость превышена')

class PoliceCar(Car):
    pass

town_car = TownCar('100', 'red', 'Audi', False)
sport_car = SportCar('200', 'black', 'BMW', False)
work_car = WorkCar('40', 'white', 'Citroen', False)
polica_car = PoliceCar('150', 'black', 'KIA', True)

town_car.show_speed()
work_car.show_speed()
sport_car.show_speed()