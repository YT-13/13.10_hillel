# Завдання 2 (опціонально +5 до роботи)
#
# Створіть словник із випадковими числовими значеннями довжиною в 20 елементів.
# Необхідно їх (числові значення) перемножити і вивести на екран згенерований на початку словник
# та результат множення чисел.



import random

list_a = [random.randint(1, 99) for i in range(20)]

list_b = [x for x in range(1, 21)]

# for x in range(1, len(list_a) + 1):
#     list_b.append(x)

print(list_b)

new_dict = dict(zip(list_b, list_a))

print(new_dict)

list_c = [list_b * 3]

