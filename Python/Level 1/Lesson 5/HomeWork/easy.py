import os


def show_dir_contents(path):
    # Отображение содержимого текущей директории
    print('\nСодержимое текущей директории:')

    for root, dirs, files in os.walk(path, topdown=True, onerror=walk_error_handler):
        for name_dir in dirs:
            print(f'\{name_dir} -- dir')
        for name_files in files:
            print(f'\{name_files} -- file')
        break


def walk_error_handler(exception_instance):
    print(f'{exception_instance}')
