# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

print('\nЗадача №1')

import os
import sys
import easy


def show_current_dir(path):
    if not path:
        path = os.getcwd()
    current_dir = os.path.basename(path)
    print(f'\nТекущая директория: {current_dir}')


def get_interface_action():
    try:
        return int(input("\nВыбирите действие:\n"
                         "1. Перейти в папку\n"
                         "2. Просмотреть содержимое текущей папки\n"
                         # "3. Удалить папку\n"
                         # "4. Создать папку\n"
                         "0. Выход\n"
                         ">>> "))
    except ValueError:
        print('Ошибка ввода повторите еще раз')
        return get_interface_action()
    except Exception as err:
        print(f'Неизвестная ошибка обратитесь к администратору {err}')
        return 0


def choose_dir():
    dir_name = input('Введите имя дериктории:\n'
                     '>>>')
    if os.path.isdir(dir_name):
        print(f'\nУспешно перешли в каталог {dir_name}')
        return dir_name
    else:
        print(f'Директории с именем {dir_name} не существует')


def run_feature(current_path):
    while True:
        show_current_dir(current_path)
        action = get_interface_action()

        if action == 0:
            print('\nBye)))')
            break

        if action == 1:
            new_dir = choose_dir()
            if new_dir:
                current_path = new_dir
        elif action == 2:
            easy.show_dir_contents(current_path)
        # elif action == 3:
        #     easy.delete_dir()
        # elif action == 4:
        #     easy.create_dir()

        if current_path == os.path.basename(start_path):
            current_path = start_path


start_path = os.getcwd()
run_feature(start_path)
