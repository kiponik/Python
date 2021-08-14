import random

class Game:
    def __init__(self):
        self.player1 = Card()
        self.player2 = Card()
        self.barrel = list(range(1, 91))
        while self.digit_check(self.player1.player_card) is True or self.digit_check(self.player2.player_card) is True:
            if self.digit_check(self.player1.player_card) is False:
                print('Вы победили')
                break
            if self.digit_check(self.player2.player_card) is False:
                print('Компьютер победил')
                break

            print('Новый Бочонок ' + str(self.barrel_generator()) + '\n' + 'Ваша Карточка' + '\n' + str(
                self.player1.visible_card) + '\n' + 'Карточка Компьютера' + '\n' + str(
                self.player2.visible_card) + '\n')
            user_input = input('Зачеркнуть цифру? y/n ')
            if self.check_condition(user_input) is False:
                print('Game Over')
                break
            else:
                self.player1.player_card = self.switch(self.player1.player_card)
                self.player1.visibility()

            self.player2.player_card = self.switch(self.player2.player_card)
            self.player2.visibility()

    def barrel_generator(self):
        self.random_index = random.randint(0, len(self.barrel) - 1)
        try:
            self.random_barrel = self.barrel[self.random_index]
            self.barrel.pop(self.random_index)
        except:
            print(self.random_index)
            print(len(self.barrel))


        return self.random_barrel

    def check_condition(self, user_input):
        self.output = user_input
        exist_check = self.player1.player_card.count(self.random_barrel)
        if exist_check == 0 and (self.output == 'y' or self.output == 'Y'):
            return(False)
        elif exist_check == 0 and (self.output == 'n' or self.output == 'N'):
            return(True)
        elif exist_check == 1 and (self.output == 'n' or self.output == 'N'):
            return(False)
        else:
            return(True)

    def switch(self, player):
        self.player_list = player
        for n, i in enumerate(self.player_list):
            if i == self.random_barrel:
                self.player_list[n] = '-'
        return self.player_list

    def digit_check(self, player_list):
        self.check_list = player_list
        for character in self.check_list:
            if isinstance(character, int):
                return True
        return False



class Card:
    def __init__(self):
        self.random_card = []
        self.player_card = []
        self.new_line = []
        for i in range(0, 3):
            random_list = random.sample(range(1, 91), 5)
            random_list.sort()
            self.player_card.extend(random_list)

        self.visibility()


    def visibility(self):
        index = 1
        for i in range(len(self.player_card)):
            self.new_line.append(self.player_card[i])
            if index == 5:
                self.random_card.append(self.new_line)
                self.new_line = []
                index = 0
            index += 1
        self.visible_card = '\n'.join([' '.join(map(str, line)) for line in self.random_card])
        self.random_card = []

game = Game()