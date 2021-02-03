# Ввод данных

result = int(input('Введите пожалуйста начальное значение для спортсмена: '))
expectedResult = int(input('Введите пожалуйста требуемый результат: '))
day = 1


# Вычисления и вывод

while result < expectedResult:
    print(day, 'день: Результат', round(result, 2))
    coefficient = result * 0.10
    result = result + coefficient
    day += 1
    if result >= expectedResult:
        print(day, 'день: Ожидаемый результат', int(expectedResult), 'достигнут с значением: ', round(result, 2))