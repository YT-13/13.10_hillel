'''
створити функцію генератор простих (освіжіть собі у памяті що таке прості числа !!!!)
чисел у дипазоні заданих двома аргументами чисел.
Вивести у консоль результат роботи функції-генератора в діапазоні
від N до Z в один рядок через прогалину. N і Z - числа діапазону які можна вибирати випадковим чином.
'''
import random

# def func(n, z):
#     for i in range(n, z+1):
#         yield i
# for k in func(5, 10):
#     print(k, end=' ')

def func(n, z):
    for i in range(n, z+1):
        yield i
n = random.randint(1, 5)
print('n = ', n)
z = random.randint(5, 10)
print('z = ', z)
for k in func(n, z):
    print(k, end=' ')

