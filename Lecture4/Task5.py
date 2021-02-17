from functools import reduce, partial

def sum_numbers(num1, num2):
    return num1 * num2


new_list = [el for el in range(100, 1000, 2)]
print(new_list)
print(reduce(sum_numbers, new_list))