# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


# Базовый клас родитель для классов
class Person:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    # Функция для подсчета урона
    def __calculate_damage(self, armor):
        return self.damage // armor

    # Функция атаки, принимает на вход 2 структуры
    def attack(self, enemy):
        damage = self.__calculate_damage(enemy.armor)
        enemy.health -= damage
        print(f'{self.name.title()} нанес {enemy.name.title()} урона {damage}, у того осталось {enemy.health} жизней.')

    # Вспомагательный меод получения текущих парметров игрока
    def to_string(self):
        print(f'name: {self.name.title()}, health: {self.health}, damage: {self.damage}, armor: {self.armor}')


class Player(Person):
    def __init__(self, name, health=100, damage=20, armor=0.5):
        Person.__init__(self, name, health, damage, armor)


class Enemy(Person):
    def __init__(self, name, health=100, damage=10, armor=0.7):
        Person.__init__(self, name, health, damage, armor)


class GameEngine:

    def start_game(self):

        # Создаем обьекты игроков
        defender = Player(self.get_player_name('обороняющегося'))
        attacker = Enemy(self.get_player_name('атакующего'))

        # Алгоритм сражения
        while defender.health > 0 and attacker.health > 0:
            attacker.attack(defender)
            attacker, defender = (defender, attacker)

        # Награждаем победителя
        if defender.health > 0:
            print(f'{defender.name} победил!')
        else:
            print(f'{attacker.name} победил!')

    def get_player_name(self, name_gamer):
        return input(f'Введите имя {name_gamer} игрока:\n>>>>>')


GameEngine().start_game()
