# Вносим данные

names_list = []
prices_list = []
quantities_list = []
pieces_list = []

# Сколько товаров хочет внести пользователь

item_quantity = int(input('Введите пожалуйста количество вносимых товаров: '))
item_list = []
item_Number = 1

# Организовываем список с кортежем из номера и словаря

while item_Number <= item_quantity:
    item_dict = {}
    item_dict['name'] = input('Введите название: ')
    item_dict['price'] = int(input('Введите цену: '))
    item_dict['quantity'] = int(input('Введите количество: '))
    item_dict['unit_of_measure'] = input('Введите единицу измерения: ')
    item_tuple = (item_Number, item_dict)
    item_list.append(item_tuple)
    names_list.append(item_dict['name'])
    prices_list.append(item_dict['price'])
    quantities_list.append(item_dict['quantity'])
    pieces_list.append(item_dict['unit_of_measure'])
    item_Number = item_Number + 1

attributes_dict = {'names': names_list, 'prices': prices_list, 'quantities': quantities_list, 'pieces': pieces_list}

# Выводим значения

print(item_list)
print(attributes_dict)