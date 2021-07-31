# first version

def exponent_maker(number, extent):
    result = number ** extent
    print(round(result, 3))

# second version

def exponent_maker_v2(number, extent):
    extent = extent * (-1)
    result = 1
    i = 0
    while i < extent:
        result = result * number
        i = i + 1
    result = 1 / result
    print(round(result, 3))

positive_number = int(input('Введите целое положительное число: '))
negative_number = int(input('Введите целое отрицательное число: '))
exponent_maker(positive_number, negative_number)
exponent_maker_v2(positive_number, negative_number)