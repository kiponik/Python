import codecs

text_dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_text = []

with open('someText.txt', 'r') as someText:
    lines = someText.readlines()
    for line in lines:
        line = line.encode('windows-1251').decode('utf-8')
        words = line.split()
        new_word = text_dictionary.get(words[0])
        words[0] = new_word
        new_line = ' '.join(map(str, words))
        new_text.append(new_line + '\n')

with codecs.open('newDictionary.txt', 'w', 'utf-8-sig') as new_dictionary:
    new_dictionary.writelines(new_text)