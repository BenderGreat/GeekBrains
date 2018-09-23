# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    color = 'Black'
    name = 'Ford'
    speed = 120
    is_police = False

    def go(self):
        print('\nМашина поехала!')

    def stop(self):
        print('\nМашина остановилась')

    def turn(self, direction):
        print(f'Машина повернулась на {direction}')


class SportCar:
    color = 'White'
    name = 'Ferrari'
    speed = 250
    is_police = False

    def go(self):
        print('\nМашина поехала!')

    def stop(self):
        print('\nМашина остановилась')

    def turn(self, direction):
        print(f'Машина повернулась на {direction}')


class WorkCar:
    color = 'Green'
    name = 'Volvo'
    speed = 80
    is_police = False

    def go(self):
        print('\nМашина поехала!')

    def stop(self):
        print('\nМашина остановилась')

    def turn(self, direction):
        print(f'Машина повернулась на {direction}')


class PoliceCar:
    color = 'Black'
    name = 'Doodge'
    speed = 250
    is_police = True

    def go(self):
        print('\nМашина поехала!')

    def stop(self):
        print('\nМашина остановилась')

    def turn(self, direction):
        print(f'Машина повернулась на {direction}')


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:

    def __init__(self, color, name, speed, is_police):
        self.color = color
        self.name = name
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print('\nМашина поехала!')

    def stop(self):
        print('\nМашина остановилась')

    def turn(self, direction):
        print(f'Машина повернулась на {direction}')