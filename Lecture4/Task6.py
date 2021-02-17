from itertools import count, cycle
from sys import argv

script_name, input_number, element1, element2 = argv

for i in count(int(input_number)):
    print(i)
    if i > 10:
        break

new_list = [element1, element2]
i = 0
for elements in cycle(new_list):
    i += 1
    print(elements)
    if i > 10:
        break