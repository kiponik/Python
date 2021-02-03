# Создаём лист

my_list = ['Test', 1, True, 1.1, 'Test2', 5, 'Test3', 6, 'Test4', 7, 'Test5']

# Вводим переменные

total = len(my_list)
i = 0

# Выполняем цикл

while i <= total:
    if i + 1 >= total: # Проверяем, если не превышенна длинна списка
        break
    elem1 = my_list[i] # Привязываем значение индекса к переменной
    elem2 = my_list[i + 1]
    my_list[i] = elem2
    my_list[i + 1] = elem1
    i = i + 2

print(my_list)