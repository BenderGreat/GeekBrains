#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random


class Player:

    def __init__(self, name):
        self.name = name
        self.card = self.create_player_card()

    def create_player_card(self):
        return Card(self.name)

    def show_card(self):
        self.card.show_player_card()

    def compare_barrel_whith_card(self, barrel):
        list_card_num = self.card.player_card[0] + self.card.player_card[1] + self.card.player_card[2]
        # print(f'{list_card_num}')
        if list_card_num.count(barrel) > 0:
            print(f'Есть такая цифра : {barrel}\n'
                  f'У игрока: {self.name}')
            self.close_cell_player_card(barrel)
        else:
            print(f'Нет такой цифры: {barrel}\n'
                  f'У игрока: {self.name}')

    def close_cell_player_card(self, barrel):
        for indx, item in enumerate(self.card.player_card):
            if item.count(barrel):
                index = item.index(barrel)
                if index >= 0:
                    self.card.player_card[indx][index] = '-'
                    self.card.show_player_card()
                    break

    def get_close_cell(self):
        list_card_num = self.card.player_card[0] + self.card.player_card[1] + self.card.player_card[2]
        return list_card_num.count('-')

class PlayerUser(Player):
    def __init__(self, name='User'):
        super().__init__(name)


class PlayerComputer(Player):
    def __init__(self, name='Computer'):
        super().__init__(name)


class Card:

    def __init__(self, name_player):
        self.name_player = name_player
        self.player_card = self.create_player_card()

    def create_player_card(self):
        matrix_card = self.create_matrix_card()
        player_card = self.fill_matrix(matrix_card)
        # self.show_player_card()
        return player_card

    def fill_matrix(self, matrix_card):
        list_barrels = []
        player_card = []
        for index, item in enumerate(matrix_card):
            card_line = []
            for indx, cell in enumerate(item):
                if cell == 1:
                    interval = self.get_interval(indx + 1)
                    while len(interval) > 0:
                        cell = random.choice(interval)
                        if not list_barrels.count(cell):
                            interval = list()

                    list_barrels.append(cell)
                card_line.append(cell)

            player_card.append(card_line)
        return player_card

    def show_player_card(self):
        print(f'\n------ Карта игрока: {self.name_player} - ----')
        for line in self.player_card:
            string = "   ".join(map(str, line))
            print(f'{string}')
        print(f'------ Карта игрока: {self.name_player} - ----\n')

    def get_interval(self, num_interval):
        interval = [num for num in range(num_interval * 10 - 10, num_interval * 10)]
        if num_interval == 1:
            interval.remove(0)
        if num_interval == 9:
            interval.append(90)
        return interval

    def get_random_list(self, one, zero):
        line = [0 for _ in range(1, 5 - zero)] + [1 for _ in range(1, 6 - one)]
        return random.sample(line, len(line))

    def create_matrix_card(self):
        matrix_card = []
        for num_line in range(1, 3):
            matrix_card.append(self.create_matrix_line())

        third_line = [sum(list(cell)) for cell in zip(matrix_card[0], matrix_card[1])]

        number_of_one = third_line.count(0)
        number_of_zero = third_line.count(2)
        random_third_line = self.get_random_list(number_of_one, number_of_zero)
        new_third_line = []

        for x in third_line:
            if x == 0:
                new_third_line.append(1)
            if x == 2:
                new_third_line.append(0)
            if x == 1:
                new_third_line.append(random_third_line.pop())

        third_line = new_third_line
        matrix_card.append(third_line)

        return matrix_card

    def create_matrix_line(self):
        random_line = [0 for _ in range(1, 5)] + [1 for _ in range(1, 6)]
        random_line = random.sample(random_line, len(random_line))
        return random_line


class Game:

    def __init__(self):
        self.list_barrels = [barrel for barrel in range(1, 91)]

    def get_random_barrel(self):
        barrel = random.choice(self.list_barrels)
        self.list_barrels.remove(barrel)
        return barrel

    def create_players(self):
        self.user = PlayerUser()
        self.computer = PlayerComputer()

    def start_game(self):
        self.create_players()
        new_game = 1
        while new_game > 0:
            self.show_players_card()
            rnd_barrel = self.get_random_barrel()
            print(f'Случайная бочка под номером: {rnd_barrel}')
            self.user.compare_barrel_whith_card(rnd_barrel)
            self.computer.compare_barrel_whith_card(rnd_barrel)
            # print(f'{self.list_barrels}')
            if self.user.get_close_cell() > 14:
                print(f'Конец игры !!! Выиграл {self.user.name}')
                new_game = 0
            elif  self.computer.get_close_cell() > 14:
                print(f'Конец игры !!! Выиграл {self.computer.name}')
                new_game = 0
            if new_game == 0:
                start_new_game = str(input('Еще один раунд Y/N?'))
                if start_new_game == 'Y':
                    self.__init__()
                    self.start_game()



    def show_players_card(self):
        self.user.show_card()
        self.computer.show_card()


game = Game()

game.start_game()
