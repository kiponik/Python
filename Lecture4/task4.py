original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def remove_duplicates(numbers):
    unique_numbers = set()
    for number in numbers:
        if original_list.count(number) > 1:
            continue
        if number not in unique_numbers:
            yield number
            unique_numbers.add(number)

print(list(remove_duplicates(original_list)))