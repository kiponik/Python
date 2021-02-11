# Вводим данные

user_input = input('Введите предложение: ')

# Вносим в список

user_list = user_input.split(' ')

# Выводим через for in и срезаем от 0 до 10

for (i, item)  in enumerate(user_list, start=1):
    print(i, item[0:10])