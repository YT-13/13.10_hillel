# Натуральні числа називаються антропоморфними якщо вони дорівнюють останнім цифрам свого квадарту.
# Наприклад 25 в квадраті еквівалентно 625.
# Напишіть програму яка запрошує число N і виводить усі антропоморфні числа що не більше за N.

# i = 5
# i_squared = i ** 2
# print(i_squared)
# if str(i_squared).endswith(str(i)):
#   pass

# number = int(input('Вdедіть число >>> '))
# for i in range(1, number):
#     if i * i < number:
#         print(i*i)
#         if i in i*i:
#             print(i*i)

number = int(input('Введіть число >>> '))
resultList = []
counter = 1
while counter <= number:
    square = pow(counter, 2)
    stringCounter = str(counter)
    stringSquare = str(square)
    if stringSquare.endswith(stringCounter):
        resultList.append(counter)
    counter += 1
print(resultList)