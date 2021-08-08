class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {}

    def __init__(self, parameter1, parameter2, parameter3, parameter4, parameter5):
        Worker.name = parameter1
        Worker.surname = parameter2
        Worker.position = parameter3
        Worker._income = {'wage': int(parameter4), 'bonus': int(parameter5)}


class Position(Worker):
    def get_full_name(self):
        print(Worker.name, Worker.surname, Worker.position)

    def get_total_income(self):
        incomes = Worker._income.values()
        print(sum(incomes))

employer = Position('Dan', 'Mat', 'engineer', '5000', '2000')

employer.get_full_name()
employer.get_total_income()