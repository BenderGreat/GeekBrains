# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.


class ToyFactory:
    __dict_class_type = {'wolf': 'Wolf', 'sun': 'Sun'}

    def __init__(self, name, color, type_toy):
        self.name = name
        self.color = color
        self.type_toy = type_toy

    def buy_materials(self):
        print(f'Закупаем метриалы для производства {self.name}')

    def sew_toy(self):
        print(f'Производим игрушку {self.type_toy}')

    def paint_toy(self):
        print(f'Красим игрушку в {self.color} цвет')

    def make_toy(self):
        self.buy_materials()
        self.sew_toy()
        self.paint_toy()
        return Toys(self.name, self.color, self.type_toy).view_toy()


class Toys:

    def __init__(self, name, color, type_toy):
        self.name = name
        self.color = color
        self.type_toy = type_toy

    def view_toy(self):
        print(f'Название {self.name}, Цвет {self.color}, Тип {self.type_toy}')


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class Wolf(Toys):
    __type_toy = 'wolf'

    def __init__(self, name, color):
        Toys.__init__(self, name, color, self.__type_toy)


class Sun(Toys):
    __type_toy = 'sun'

    def __init__(self, name, color):
        Toys.__init__(self, name, color, self.__type_toy)
