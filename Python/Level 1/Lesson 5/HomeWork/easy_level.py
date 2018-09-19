# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

import sys


def get_list_dir_in_current_path(show_title=True):
    # Получение списка поддиректорий в текушей директории
    list_dir_current_path = list()
    if show_title:
        print(f'\nТекущая директория - {os.getcwd()}')
        print('Список поддиректорий в текущей директории:')

    for root, dirs, files in os.walk('.', topdown=True):
        list_dir_current_path = dirs
        for name_dir in dirs:
            print(f'\{name_dir}')
        break

    if not list_dir_current_path and show_title:
        print('\nВ данной директории нет поддиректорий')

    return list_dir_current_path


print('\nЗадача №1 и Задача №2')

list_dir = ['dir_' + str(num) for num in range(1, 10)]
current_path = os.getcwd()

print(f'\nСоздадим поддиректории в директории {current_path}:\n')
for name in list_dir:
    try:
        os.mkdir(name)
        print(f'Директория \{name} - создана')
    except FileExistsError:
        print(f'Директория \{name} уже существует!')

get_list_dir_in_current_path()

print(f'\nУдалим поддиректории в директории {current_path}:\n')
for name in list_dir:
    try:
        os.rmdir(name)
        print(f'Директория \{name} - удалена')
    except OSError:
        print(f'Директория \{name} не может быть удалена.'
              '\n Возможные причины:'
              '\n - Директория не существует'
              '\n - Директория содержит файлы'
              '\n - прочее')

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


print('\nЗадача №3')

file_name = os.path.basename(sys.argv[0])

print(f'\nСоздание копии файла {file_name}')

with open(file_name, 'r', encoding='UTF-8') as origin_file:
    new_file = 'copy_' + file_name
    if os.path.isfile(new_file):
        print(f'\nКопия {new_file} файла {file_name} существует.')
    else:
        with open(new_file, 'w', encoding='UTF-8') as copy_file:
            try:
                copy_file.write(origin_file.read())
                print(f'\nКопия {new_file} файла {file_name} - создана.')
            except Exception as err:
                print(f'{err}')
