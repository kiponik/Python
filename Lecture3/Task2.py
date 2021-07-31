def user_details(a, b, c, d, e):
    print(
        "Ваше имя: " + a + "Ваша фамилия: " + b + "Ваш год рождения: " + c + "Ваш email: " + d + "Ваш номер телефона: " + e, sep=' ')


name = input('Введите имя ')
surname = input('Введите фамилия ')
birth_date = input('Введите ваш год рождание ')
email = input('Введите почтовый ящик ')
phone_number = input('Введите ваш номер телефона ')

user_details(a=name, b=surname, c=birth_date, d=email, e=phone_number)
