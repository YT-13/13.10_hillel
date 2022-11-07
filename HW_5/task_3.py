# Программа запитує ввід з клавіатури цілі числа по черзі - до того часу поки не буде введено 0.
# Як тільки буде введено 0 программа повинна порахувати і вивести в термінал
#
# Сумму чисел
# Середнє арифметичне усіх введених чисел (не враховуючи останнього 0)
# Визначити максимальне і мінімальне занчення
# Визначити кількість парних та кількість не парних чисел
list_x = []
while True:
    x_input = int(input('Введіть будь-яке невідємне число >>> '))

    if x_input == 0:
        break

    list_x.append(x_input)

sum_input = sum(list_x)
print(f'Сума введених чисел = {sum_input}')

print(f'Cереднє арифметичне (крім завершального числа 0) = {sum_input / len(list_x)}')

list_x.sort()
print(f'Мінімальне значення = {list_x[0]}, а максимальне значення = {list_x[-1]}')

para = []
nepara = []
for elem in list_x:
    if elem % 2 == 0:
        para.append(elem)
    else:
        nepara.append(elem)
print(f'Кількість парних елементів = {len(para)}')
print(f'Кількість непарних елементів = {len(nepara)}')