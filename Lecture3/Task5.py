

print('Для выхода введите Q')

# Ввод данных

numbers_input = input('Введите лист чисел через пробел: ')
string_list = numbers_input.split(' ')

# Проверка на остановку

if 'Q' in string_list:
    quit_index = string_list.index('Q')
    del string_list[quit_index:]
elif 'q' in string_list:
    quit_index = string_list.index('q')
    del string_list[quit_index:]

# Перевод в int

numbers_map = map(int, string_list)
integer_list = list(numbers_map)
print(sum(integer_list))