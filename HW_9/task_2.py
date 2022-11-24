#2
# Напишіть програму, яка виводить квадратну матрицю розміру N на N заповнену випадковими числами. N = запросити у користувача
# Вивести значення у вигляді матриці чисел.
# Вивести в термінал - суму чисел по діагоналі
# Вивест на єкран суму чисел остнанього стовбця. (
# Можна використити вираз і функцію sum()

import random

n = int(input('Введіть число >>> '))

list_a =[[random.randint(0, n) for x in range(n)] for i in range(n)]

for elem in range(n):
    print(list_a[elem])

new_list = []

for i in range(n):
    new_list.append(list_a[i][i])

print('Cума чисел по діагоналі = %s' % sum(new_list))

print('Сума чисел остнанього стовбця = {}'.format(sum(list_a[len(list_a)-1])))

