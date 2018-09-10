# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

first_var = 'Моя первая переменная Pyton'  # first variable type str
second_var = 2  # second variable type int
third_var = True  # third variable type bool

print('\nfirst_var = ', first_var, ' Type = ', type(first_var))
print('\nfirst_var = ', second_var, ' Type = ', type(second_var))
print('\nfirst_var = ', third_var, ' Type = ', type(third_var))

first_input = input('\nВведите любые сиволы ')
print('\nВы ввели ', first_input, '\nТип данных', type(first_input))

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

first_input = int(input('\nВведите любое число '))
print('\nВы ввели ', first_input, '\nПрибавим к введенному числу 2 \nИтого: ', first_input + 2)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

input_age = int(input('\nВведите ваш возраст '))

if input_age > 17:
    print('Доступ разрешен ')
else:
    print('Извините, пользование данным ресурсом только с 18 лет ')
