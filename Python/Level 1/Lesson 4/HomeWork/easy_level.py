# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

print('Задание №1\n')

import_list = [num for num in range(15)]  # OR simple list(range())

print(f'Исходный список целых чисел {import_list} ')

generate_list = [num ** 2 for num in import_list]

print(f'Новый список квадратов исходного {generate_list}\n')

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print('Задание №2\n')
fruits_list_one = ['mangosteen', 'apple', 'orange', 'lychee', 'banana']
fruits_list_tow = ['mangosteen', 'passionfruit', 'orange', 'pineapple', 'melon']

print(f'Исходные списки фруктов:\n 1. {fruits_list_one}\n2. {fruits_list_tow}')

joint_fruit_list = [fruit for fruit in fruits_list_one if fruit in fruits_list_tow]

print(f'Фрукты присутствуюшие в обеих списках:\n {joint_fruit_list}\n')

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3, Элемент положительный, Элемент не кратен 4
# + Элемент положительный
# + Элемент не кратен 4

print('Задание №3\n')


import_list = [num for num in range(-16,16)]

print(f'Произваольный список чисел:\n {import_list}')
generate_list = [num for num in import_list if not num / 3 - int (num / 3) if num == abs(num) if num % 4]

print(f'Список cоcтавленный из исходного:\n {generate_list}\nСписок удовлетворяющий следующим условиям:\nЭлемент кратен 3 \nЭлемент положительный\nЭлемент не кратен 4')