def in_divide(a, b):
    if b != 0:
        print(a / b)
    else:
        print('Деление на ноль запрещено')


first_input = int(input('Input the first number '))
second_input = int(input('Input the second number '))

in_divide(first_input, second_input)
