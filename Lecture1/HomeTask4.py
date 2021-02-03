# Ввод положительного числа

positiveNumber = int(input("Введите пожалуйста целое положительное число: "))

largeNumber = 0

# Проверка на самую большую цифру в числе

while(positiveNumber > 0):
    checker = positiveNumber % 10
    if largeNumber < checker:
        largeNumber = checker
    positiveNumber = positiveNumber / 10

# Вывод

print(int(largeNumber))