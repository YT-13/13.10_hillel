#3
# Напишіть програму, Яка генерує список із 15 випадкових чисел.
# Виведіть:
# Так - якщо сума непарних чисел у списку більша за суму парних чисел
# Ні - у всіх інших випадках

import random

list_a = [random.randint(0, 25) for i in range(15)]

list_x = [] #парні числа

list_y =[] #непарні числа

for l in list_a:
    if l % 2 == 0:
        list_x.append(l)
    else:
        list_y.append(l)

# print('Згенерований список з 15 елементів: ', list_a)

# print('Список парних чисел: ', list_x)

# print('Список непарних чисел: ', list_y)

if sum(list_y) > sum(list_x):
    print('ТАК')
else:
    print('НІ')