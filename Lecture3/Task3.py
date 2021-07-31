def two_max(number1, number2, number3):
    numbers = [number1, number2, number3]
    getIndex = numbers.index(min(numbers))
    del numbers[getIndex]
    print(sum(numbers))

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

two_max(a, b , c)