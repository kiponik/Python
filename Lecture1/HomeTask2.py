# Запрос ввода времени в секундах

seconds = int(input('Введите пожалуйста секунды: '))
minutes = 0
hours = 0

# СИ в минуты

while seconds > 59:
    minutes += 1
    seconds = seconds - 60
    while minutes > 59:
        hours += 1
        minutes = minutes - 60

# Вывод результата

print(hours, minutes, seconds, sep=':')