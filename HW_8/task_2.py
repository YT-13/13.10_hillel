# Завдання 2
# Запросити у користувача ввести речення у якому більше 2х слів.
# Розділити речення на список рядків (використовуючи метод рядку split(" ") - де параметром вказано " ").
# Видалити елементи списку якщо вони містять пусті рядки.
# Відсортирувати рядки у списку.
# Вивести дані зі списку в 2 колонки де перша колонка це індекс cписку а 2га колонка це елемент відсортированого списку.
# Вивести кількість слів.

input_words = input('Введіть декілька слів через пробіл >>> ')
input_words = input_words.split(' ')

print('Отриманий список >>> {}\n'.format(input_words))

if '' in input_words:
    count = input_words.count('')
    i = 1
    while True:
        input_words.remove('')
        if i >= count:
            break
        i+=1
print('Видалили пусті рядки зі списку >>> {}\n'.format(input_words))

input_words = sorted(input_words)
print('Відсортований список = {}\n'.format(input_words))

for i in range (0, len(input_words)):
    print('{:>2}-й елемент списку = {}'.format(i+1, input_words[i]))

print('\n'
      'Кількість слів в цьому списку = ', len(input_words))