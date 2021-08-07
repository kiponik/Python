input_text = input('Введите предложение: ')
new_text = []
while input_text != '':
    new_text += [input_text + "\n"]
    input_text = input(': ')

file_object = open('text.txt', 'w')
file_object.writelines(new_text)
file_object.close

file_object = open('text.txt', 'r')
print(file_object.read())
file_object.close()