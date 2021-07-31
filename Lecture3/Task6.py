def lower_to_up(input_text):
    for input_word in input_text:
        input_characters = list(input_word)
        first_char = input_word[0].upper()
        input_characters[0] = first_char
        input_word = ''.join(input_characters)
        print(input_word)

text_input = input("Введите слово: ")
text_split = text_input.split(' ')

lower_to_up(text_split)