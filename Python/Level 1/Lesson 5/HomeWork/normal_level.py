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
import easy

print('\nЗадача №1')


def get_interface_action():
    # Создание меню сервиса
    try:
        return int(input("\nВыбирите действие:\n"
                         "1. Перейти в папку\n"
                         "2. Просмотреть содержимое текущей папки\n"
                         "3. Удалить папку\n"
                         "4. Создать папку\n"
                         "0. Выход\n"
                         ">>> "))
    except ValueError:
        print('Ошибка ввода повторите еще раз')
        return get_interface_action()
    except Exception as err:
        print(f'Неизвестная ошибка обратитесь к администратору {err}')
        return 0


def choose_dir():
    # Пункт меню Перейти в папку
    dir_name = input('Введите имя дериктории:\n'
                     '>>>')
    easy.change_current_dir(dir_name)


def create_dir():
    # Пункт меню Создать папку
    name = input('Введите имя новой папки:\n>>> ')
    easy.create_new_dir(name)


def delete_dir():
    # Пункт меню Удалить папку
    name = input('Введите имя папки которую необходимо удалить:\n>>> ')
    easy.delete_dir(name)


def run_feature():
    # Алгоритм сервиса
    while True:
        easy.show_current_dir()
        action = get_interface_action()

        if action == 0:
            print('\nBye)))')
            break
        elif action == 1:
            choose_dir()
        elif action == 2:
            easy.show_dir_contents()
        elif action == 3:
            delete_dir()
        elif action == 4:
            create_dir()


run_feature()
