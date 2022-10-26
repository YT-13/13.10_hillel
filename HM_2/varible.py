third_number = second_number
second_number = first_number
first_number = third_number

print(first_number, second_number)

# заміна значень 2х змінних використовуючи властивості python - рузультат вивести на/в термінал
first_number = 13
second_number = 19
first_number, second_number = second_number, first_number

print(first_number, second_number)

# (завдання з зірочкою +3 бали до завдання) заміна значень 2 змінних не використівуючи 2х попредніх варіантів.
first_number = 13
second_number = 19
first_number = first_number + second_number
second_number = first_number - second_number
first_number = first_number - second_number

print(first_number, second_number)