class Road:
    _length = ''
    _width = ''

    def __init__(self, parameter1, parameter2):
        _length = parameter1
        _width = parameter2
        result = int(_length) * int(_width) * 25 * 5
        print(result, 'T')


test = Road('5', '6')