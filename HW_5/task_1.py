# Вввести натуральне число і впевнитись що в ньому є 2 однакові цифри (не обовязково такі що стоять разом)
# Наприклад:
# input
# number:
# 123452
# Так
# input
# number:
# 123456
# Ні

input_number = input('Введіть натуральне число >>> ')
set_number = set(input_number)
if len(input_number) == len(set_number):
    print('NO')
else:
    print('YES')







