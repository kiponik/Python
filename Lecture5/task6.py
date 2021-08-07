import codecs
lessons_dictionary = {}

with codecs.open('lessons.txt', 'r', 'utf-8-sig') as f:
    lines = f.readlines()
    for line in lines:
        words = line.split(' ')
        l = len(words[0])
        remover = words[0][:l-1]
        lesson_name = remover
        number_sum = []
        for word in words:
            if (word[0].isdigit()):
                split_number = word.split("(", 1)
                get_number = int(split_number[0])
                number_sum.append(get_number)
        lessons_dictionary[lesson_name] = sum(number_sum)

print(lessons_dictionary)