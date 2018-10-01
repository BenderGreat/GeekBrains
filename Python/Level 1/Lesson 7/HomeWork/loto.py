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


# Базовый класс игрока
class Player:

    def __init__(self, name):
        self.name = name
        self.card = self.create_player_card()
        self.list_card_num = self.card.player_card[0] + self.card.player_card[1] + self.card.player_card[2]

    # Создание карты игрока
    def create_player_card(self):
        return Card(self.name)

    # Отображение карты игрока
    def show_card(self):
        self.card.show_player_card()

    # Поиск числа в карте игрока
    def compare_barrel_whith_card(self, barrel, show=False):
        if self.list_card_num.count(barrel) > 0:
            if show:
                print(f'\nУ игрока: {self.name}\n'
                      f'В карте присутствует число: {barrel}')
            return True
        else:
            if show:
                print(f'\nУ игрока: {self.name}\n'
                      f'В карте нет числа: {barrel}')
            return False

    # Удаление числа из карты игрока (Вычеркивание)
    def close_cell_player_card(self, barrel):
        for indx, item in enumerate(self.card.player_card):
            if item.count(barrel):
                index = item.index(barrel)
                if index >= 0:
                    self.card.player_card[indx][index] = '-'
                    # self.card.show_player_card()
                    break

    # Подсчет количества зачеркнутых позицый в карточке игрока
    def get_close_cell(self):
        return self.list_card_num.count('-')


# Дочерний класс игрока (Пользователь)
class PlayerUser(Player):

    def __init__(self, name='User'):
        super().__init__(name)


# Дочерний класс игрока (Компьютер)
class PlayerComputer(Player):

    def __init__(self, name='Computer'):
        super().__init__(name)


# Класс для работы с картой игрока
# При создании карты игрока использовались следующие условия:
# - все числа уникальные
# - в одном столбце не должно быть более 2 чисел
# - интервалы чисел по столбцам ( 1 : [1:9],  9: [80:90] для всех остальных по формуле n : [n*10: n*10+9])
# - недолжно быть пустых столбцов!!! Если это условие не использовать то можно реализовать более простой метод формирования карточек.
# Алгоритм формирования карточки след:
# 1. Созданее матрицы карты со занчениями 0 и 1
# 2. Заполнение ячеек с 1 случайными числами из соответствующего интервала

class Card:

    def __init__(self, name_player):
        self.name_player = name_player
        self.player_card = self.create_player_card()

    # Формирование карты игрока
    def create_player_card(self):
        matrix_card = self.create_matrix_card()
        player_card = self.fill_matrix(matrix_card)
        return player_card

    # Запонение матрицы карты случайными числами
    # Заполняем ячейки числами из указанного интервала для данной ячейки карточки
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

    # Отображение карты игрока
    def show_player_card(self):
        print(f'\n------ Карта игрока: {self.name_player} - ----')
        for line in self.player_card:
            string = "   ".join(map(str, line))
            print(f'{string}')
        print(f'------ Карта игрока: {self.name_player} - ----\n')

    # Получение интервалов для столбцов карты
    # Необходимы для заполнения матрицы слчайными числами
    def get_interval(self, num_interval):
        interval = [num for num in range(num_interval * 10 - 10, num_interval * 10)]
        if num_interval == 1:
            interval.remove(0)
        if num_interval == 9:
            interval.append(90)
        return interval

    # Создание строки с произвольным количеством 1 - one и 0 - zero
    def get_random_list(self, one, zero):
        line = [0 for _ in range(1, 5 - zero)] + [1 for _ in range(1, 6 - one)]
        return random.sample(line, len(line))

    # Формирование матрицы для карты пользователя (произваольное расположение 0 и 1 уазывающих на размещение чисел на карте)
    def create_matrix_card(self):
        matrix_card = []

        # Создаем матрицу с 2 столбцами
        for num_line in range(1, 3):
            matrix_card.append(self.create_matrix_line())

        # Формируе третий столбец матрици исходя из предыдущих строк
        # Складываем 1 и 2 строку
        third_line = [sum(list(cell)) for cell in zip(matrix_card[0], matrix_card[1])]

        # Формируем строку со случайным расположением 1 и 0
        number_of_one = third_line.count(0)
        number_of_zero = third_line.count(2)
        random_third_line = self.get_random_list(number_of_one, number_of_zero)
        new_third_line = []

        # Формируем конечную строку
        for x in third_line:
            if x == 0:
                new_third_line.append(1)  # Заменяем 0 на единицу для того чтобы небыло пустых столюцов в карточке
            if x == 2:
                new_third_line.append(0)  # Заменяем 2 на 0 для тго чтобы небыло трех чисел в одном столбце
            if x == 1:
                new_third_line.append(random_third_line.pop())  # Заменяем значения в ячейках на случайные значения

        third_line = new_third_line
        matrix_card.append(third_line)
        return matrix_card

    # Формируем строку матрицы карты из 5 единиц и 4 нулей
    # Далее перемешиваем их в случайном порядке
    def create_matrix_line(self):
        random_line = [0 for _ in range(1, 5)] + [1 for _ in range(1, 6)]
        random_line = random.sample(random_line, len(random_line))
        return random_line


# Класс игрового процесса
class Game:

    def __init__(self):
        self.create_players()
        self.list_barrels = [barrel for barrel in range(1, 91)]

    # Получение случайного боченка с числом
    def get_random_barrel(self):
        barrel = random.choice(self.list_barrels)
        self.list_barrels.remove(barrel)
        return barrel

    # Создание игроков
    def create_players(self):
        self.user = PlayerUser()
        self.computer = PlayerComputer()

    # Оновоной алгоритм игры
    def start_game(self):
        new_game = 1
        while new_game > 0:
            print('\n------------------------- Новый раунд!!! ----------------------------------')
            self.show_players_card()
            rnd_barrel = self.get_random_barrel()
            print(f'Случайная бочка под номером: {rnd_barrel}')

            user_ans = input('Вычеркнуть число Y/N?  >>>> ')

            if not self.user.compare_barrel_whith_card(rnd_barrel, True) and user_ans == 'Y':
                print('Вы проиграли т.к. на карточке нет такого числа')
                new_game = 0
            elif self.user.compare_barrel_whith_card(rnd_barrel) and user_ans != 'Y':
                print('Вы проиграли т.к. не зачеркнули число в карточке')
                new_game = 0
            elif self.user.compare_barrel_whith_card(rnd_barrel) and user_ans == 'Y':
                self.user.close_cell_player_card(rnd_barrel)

            if new_game != 0:
                if self.computer.compare_barrel_whith_card(rnd_barrel, True):
                    self.computer.close_cell_player_card(rnd_barrel)

                num_close_cell_user = self.user.get_close_cell()
                num_close_cell_computer = self.computer.get_close_cell()

                if num_close_cell_user > 14:
                    print(f'Конец игры !!! Выиграл {self.user.name}')
                    new_game = 0
                elif num_close_cell_computer > 14:
                    print(f'Конец игры !!! Выиграл {self.computer.name}')
                    new_game = 0
                elif num_close_cell_user > 14 and num_close_cell_computer > 14:
                    print(f'Конец игры !!! Ничья.')
                    new_game = 0

            if new_game == 0:
                start_new_game = str(input('\nНачать игру заново Y/N? >>>> '))
                if start_new_game == 'Y':
                    self.__init__()
                    new_game = 1

        print('\nBye))))))')

    # Отображение карточек игроков
    def show_players_card(self):
        self.user.show_card()
        self.computer.show_card()


game = Game()

game.start_game()
