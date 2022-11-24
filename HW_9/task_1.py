# Напишіть програму, яка виводить квадратну матрицю розміру N на N.
# У кожному непарному рядку матриці йдуть числа від -N до -1, а в кожному парному — просто числа, що дорівнюють номеру цього рядка.
#
# N = запросити у користувача
# Вивести результат у вигляді матриці чисел.
# +2 бала до роботи якщо будете використовувати форматуваня так щоб числа які мають більше цифр не спотворювали візуальне представлення матриці.

import random
n = int(input('Введіть число >>> '))
# list_a =[[random.randint(-n, -1) for i in range(n)]for x in range(n) if x % 2 == 0]
#
# print(list_a)
#
# for elem in range(n):
#     print(list_a[elem])

list_a =[]
for i in range(n):
    if i % 2 == 0:
        list_a.append([random.randint(-n, -1) for x in range(n)])
    else:
        list_a.append([i+1 for x in range(n)])

for elem in range(n):
   print('{:3.2f}'.format(list_a[elem]))