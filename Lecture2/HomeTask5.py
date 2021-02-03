# Вносим данные

my_list = [7, 5, 5, 3, 2]

user_input = int(input('Введите пожалуйста новый элемент рейтинга: '))

counter = 0

# Вводим функцию для проверки индекса

for i in my_list:
    if user_input == i:
        inherit_index = counter
    counter = counter + 1

# Используем значения для вноса данных в список

my_list.insert(inherit_index, user_input)

print(my_list)