# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def format_user_information(name, age, city):
    print(f'{name.title()}, {int(age)} год(а), проживает в городе {city.title()}')


name = input('Введите ваше Имя: ')
age = input('Введите Ваш возраст: ')
city = input('Введите город проживания: ')

format_user_information(name, age, city)


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def get_max_number(num_first, num_second, num_third):
    max_num = max([num_first, num_second, num_third])
    print(f'Наибольшее число: {max_num}')


print('Введите три произвольных числа: \n')

list_num_in_word = {'first': 'First', 'second': 'Second', 'third': 'Third'}

for index, value in list_num_in_word.items():
    list_num_in_word[index] = int(input(f'{index.title()} = '))

get_max_number(list_num_in_word['first'], list_num_in_word['second'], list_num_in_word['third'])


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def get_max_string(*list_strings):
    max_string = max(*list_strings, key=len)
    print(f'Самая длинная строка: {max_string}')


list_string = ['dfsdf', 'dfsd dfsd78', '897idjhsuyyu', '76yhgrbvy5']

get_max_string(list_string)
