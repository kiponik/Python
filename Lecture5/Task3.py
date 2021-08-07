with open('employees.txt', 'r') as employees:
    lines = employees.readlines()
    for line in lines:
        words = line.split();
        if int(words[1]) < 20000:
            print(words[0])