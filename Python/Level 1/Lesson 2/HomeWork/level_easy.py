__author__ = 'Perfiliev Dmitry'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits_list = ['mangosteen', 'apple', 'orange', 'lychee', 'banana']

print("\nИспользуем f для вывода в print: \n")

n = 0
while n < len(fruits_list):
    print(f"{n + 1}. {fruits_list[n].title()}")
    n += 1

print("\nИспользуем .format() для вывода в print: \n")

n = 0
for fruit in fruits_list:
    print("{}. {}".format(n + 1, fruit.title()))
    n += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

vegetables_list = ['potato', 'tomato', 'banana', 'apple', 'carrot']

print('\nСписок овощей  и фруктов:')
n = 0
for veg in vegetables_list:
    print(f"{n + 1}. {veg.title()}")
    n += 1

print('\nУдалим из списка фрукты')

for fruit in fruits_list:
    if fruit in vegetables_list:
        vegetables_list.remove(fruit)

print('\nСписок овощей:')
n = 0
for veg in vegetables_list:
    print(f"{n + 1}. {veg.title()}")
    n += 1

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

int_numbers_list = [4, 6, 3, 24, 783, 345]

new_number_list = list()

print(f'\nИсходный список целых чисел:\n {int_numbers_list}')

for num in int_numbers_list:
    if num % 2:
        new_number_list.append(num * 2)
    else:
        new_number_list.append(num / 4)

print(f'\nИсходящий список чисел \n {new_number_list}')
