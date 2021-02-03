# Ввод данных

proceeds = int(input('Введите пожалуйста вашу выручку: '))
costs = int(input('Введите пожалуйста ваши издержки: '))
profitability = 0
netProfit = proceeds - costs
staff = 0
profitPerPerson = 0

# Проверка и вывод

if proceeds > costs:
    print('В этот раз у вас прибыль')
    profitability = netProfit / proceeds * 100
    print('Рентабельность выручки составляет: ', profitability, '%')
    staff = int(input('Введите пожалуйста количество сотрудников: '))
    profitPerPerson = netProfit / staff
    print('Прибыль фирмы в расчёте на одного сотруднки составляет: ', int(profitPerPerson))
elif proceeds == costs:
    print('Ваша прибыль покрыла ваши расходы')
else:
    print('В этот раз у вас убыток')