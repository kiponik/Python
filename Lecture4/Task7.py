def fact(x):
    a = 1
    for i in range(1, x + 1):
        a *= i
        yield a

for x in fact(3):
    print(x)
