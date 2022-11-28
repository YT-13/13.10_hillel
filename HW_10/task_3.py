# Завдання 3 (опціонально +5 до роботи )
#
# Створіть словник використовуючи генератор словника, у якому ключами будуть числа від 1 до 10,
# а значеннями ці числа, зведені в куб.

keys = [x for x in range(1, 11)]
print(keys)

value = [x ** 2 for x in range(1, 11)]
print(value)

result_dict = dict(zip(keys, value))
print(result_dict)