import random

# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

# Формулировка данного задания не совсем понятна
'''
denominators_tuple = tuple(i for i in range(2, 10))
divider_list = [i for i in range(2, 100)]
i = 0

while len(divider_list) > 0:
    divider = divider_list.pop()
    for denominator in denominators_tuple:
        if not (divider % denominator):
            i += 1
            break

print(f'Количество чисел в диапазоне от 2 до 99, кратных любому из чисел в диапазоне от 2 до 9 равно {i}')
'''
# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
'''

def is_even(e_num):
    return False if int(e_num) % 2 else True


def get_index_even_num_list(simple_list):
    index_even = list()
    if is_even(simple_list[0][1]):
        index_even.append(simple_list[0])
    if len(simple_list) > 1:
        index_even.extend(get_index_even_num_list(simple_list[1:len(simple_list)]))

    return index_even


num_list = [random.randint(1, 100) for i in range(0, 10)]

enum_num_list = [t for t in enumerate(num_list)]
index_list_num = get_index_even_num_list(enum_num_list)
index_list = [i for i, n in index_list_num ]

print(f'{num_list}')
print(f'{index_list_num}')
print(f'{index_list}')
'''
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

num_list = [random.randint(1, 100) for i in range(0, 10)]

print(f'Исходный список: {num_list}')

min_num = min(num_list)
max_num = max(num_list)

index_min = num_list.index(min_num)
index_max = num_list.index(max_num)

(num_list[index_min], num_list[index_max]) = (max_num, min_num)

print(f'Измененный список: {num_list}')
'''
# 4. Определить, какое число в массиве встречается чаще всего.
'''
nums_list = [random.randint(-100, 100) for num in range(0, 100)]
nums_set = list(set(nums_list))

result = res = list()
num_count = max_count = 0

print(f'Исходный список: {nums_list}')
print(f'Список уникальных чисел исходного списка: {nums_set}')

while len(nums_set) > 0:

    num = nums_set.pop()
    num_count = nums_list.count(num)

    if max_count < num_count:
        res = [(num, num_count)]
        max_count = num_count
    elif max_count == num_count:
        res.append((num, num_count))

    result.append((num, num_count))

print(f'Список числел встречающихся чаще всего с указанием индекса: {res}')
print(f'Исходный список с индексами: {result}')
'''

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''
def get_negative_nums_list(n_list):
    return list(filter(lambda x: x < 0, n_list))


nums_list = [random.randint(-20, 20) for num in range(0, 20)]

negative_nums_list = get_negative_nums_list(nums_list)
negative_nums_list.sort()

max_num = max(negative_nums_list)

print(f'Исходный список: {nums_list}')
print(f'Сортированный список отрицательных чисел: {negative_nums_list}')
print(f'Наибольшее отрицательное число в исходном списке = ({max_num} индекс {nums_list.index(max_num)})')
'''

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
'''
nums_list = [random.randint(-20, 20) for num in range(0, 20)]

print(f'Исходный список: {nums_list}')

index_min = nums_list.index(min(nums_list))
index_max = nums_list.index(max(nums_list))

if index_min > index_max:
    (index_min, index_max) = (index_max,index_min)

sum_list = nums_list[index_min + 1:index_max]

sum = sum(sum_list)

print(f'Суммируемый список: {sum_list}')
print(f'Сумма чисел между максимальным и минимальным числами  = {sum}')
'''

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
'''
nums_list = [random.randint(-20, 20) for num in range(0, 20)]

print(f'Исходный список: {nums_list}')

min_num_one = min(nums_list)
nums_list.remove(min_num_one)
min_num_two = min(nums_list)

print(f'Минимальные элементы списка One:{min_num_one} Two:{min_num_two}')
'''

# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
'''
matrix = [list(random.randint(0, 100) for x in range(0, 4)) for y in range(0, 4)]
print(f'Исходная матрица: {matrix}')

for x in range(0, len(matrix)):
    matrix[x].append(sum(matrix[x]))

print(f'Полученная матрица:')
for line in matrix:
    print(f'{line}')
'''

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''
matrix = [list(random.randint(0, 100) for x in range(0, 4)) for y in range(0, 4)]

print(f'Исходная матрица:')
for line in matrix:
    print(f'{line}')

min_nums_list = list()

for x in range(0, 4):
    min_nums_list.append(min(num[x] for num in matrix))

print(f'Минимальные элементы столбцов = {list(enumerate(min_nums_list, 1))}')
print(f'Максимальный элемент из минимальных элементов столюцов = {max(min_nums_list)}')
'''
