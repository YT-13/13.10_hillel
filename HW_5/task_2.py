# Натуральні числа називаються антропоморфними якщо вони дорівнюють останнім цифрам свого квадарту.
# Наприклад 25 в квадраті еквівалентно 625.
# Напишіть програму яка запрошує число N і виводить усі антропоморфні числа що не більше за N.



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