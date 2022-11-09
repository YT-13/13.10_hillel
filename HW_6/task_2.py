# Користувач вводить окремо рядок (string) і один символ (char).
# Необхідно здійснити пошук у рядку `string` всіх символів `char`.
# Для вирішення потрібно використовувати тільки функцію `find()`(rfind()), оператори `if` і `for`(while)
input_str = input('Введіть реченння >>> ')
input_char = input('Введіть символ >>> ')
index = 0
for i in range(len(input_str)):
    index = input_str.find(input_char, index + 1)
    if index == -1:
        break
    print(index)