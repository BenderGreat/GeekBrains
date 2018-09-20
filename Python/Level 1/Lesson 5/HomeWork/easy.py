import os


def show_dir_contents():
    # Отображение содержимого текущей директории
    path = os.getcwd()
    print('\nСодержимое текущей директории:')

    for root, dirs, files in os.walk(path, topdown=True, onerror=walk_error_handler):
        for name_dir in dirs:
            print(f'\{name_dir} -- dir')
        for name_files in files:
            print(f'\{name_files} -- file')
        if not dirs and not files:
            print('\nВ директории нет файлов и папок')
        break


def walk_error_handler(exception_instance):
    # Обработчик ошибок show_dir_contents os.walk - отображение содержимого текущей директории
    print(f'{exception_instance}')


def change_current_dir(dir_name):
    # Смена текущей дирректории
    if os.path.isdir(dir_name):
        os.chdir(dir_name)
        print(f'\nУспешно перешли в каталог: {show_current_dir(False)}')
    else:
        print(f'Директории с именем: {dir_name} - не существует')


def show_current_dir(show=True):
    # Выводим текушую дирректорию
    path = os.getcwd()
    current_dir = os.path.basename(path)
    if show:
        print(f'\nТекущая директория: {path}')
    return current_dir


def create_new_dir(name):
    # Создание поддиректории
    if os.path.isdir(name):
        print(f'Невозможно создать. Поддиректория с именем: {name} - уже существует')
    else:
        try:
            os.mkdir(name)
            print(f'Поддиректория {name} - успешно создана')
        except Exception as arr:
            print(f'При создании подкатегории возникла ошибка - {arr}')


def delete_dir(name):
    # Удаление поддиректории
    if not os.path.isdir(name):
        print(f'Невозможно удалить. Поддиректории с именем: {name} - не существует')
    else:
        try:
            os.rmdir(name)
            print(f'Поддиректория {name} - успешно удалена')
        except Exception as arr:
            print(f'При удалении подкаталога возникла ошибка - {arr}')
