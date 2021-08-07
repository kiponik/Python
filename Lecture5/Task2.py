with open('task2text.txt', 'r') as task2text:
    lines = task2text.readlines()
    print("Lines", len(lines))
    for line in lines:
        words = line.split();
        print(len(words))