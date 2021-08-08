import time

class TrafficLight:
    __color = ''
    def running(self):
        while True:
            __color = 'красный'
            print(__color)
            time.sleep(7)
            __color = 'желтый'
            print(__color)
            time.sleep(2)
            __color = 'зеленый'
            print(__color)
            time.sleep(3)


test = TrafficLight()
test.running()