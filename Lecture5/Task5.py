with open('listOfNumbers.txt', 'w') as numbers_list:
    input_text = input('Введите числа разделенные пробелами: ')
    numbers_list.write(input_text)

with open('listOfNumbers.txt', 'r') as get_numbers:
    numbers = get_numbers.readline()
    numbers_list = []
    numbers_list = " ".join(numbers).split()
    integer_map = map(int, numbers_list)
    print(sum(integer_map))