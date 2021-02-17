original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []

for index in range(len(original_list)):
    try:
        if original_list[index + 1] > original_list[index]:
            new_list.append(original_list[index + 1])
    except:
        pass

print(new_list)