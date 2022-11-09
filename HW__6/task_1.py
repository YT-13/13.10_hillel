# Написати програму, яка запитує у користувача два слова через пробіл.
# Визначити що введено саме 2 слова - якщо ні то запросити ввести те, що потрібно ще раз.
# Програма друкує слова в порядку прямування, але вони повинні бути перевернуті і кожне слово повинно починатися з великого символу,
# а всі інші були приведені до нижнього регістру.
# Наприклад:
#     “My Bag’
# Результат:
#     “Ym Gab”
while True:
    two_words = input('Введіть два слова через пробіл >>> ').strip()

    # if ' ' == 1 in two_words:
    if two_words.count(' ') == 1:
        two_words = two_words.split(' ')
        first_word = two_words[0]
        second_word = two_words[1]
        print(first_word[::-1].capitalize(), second_word[::-1].capitalize())
        break
    else:
        print('Некоректний ввід, потрібно ввести два слова через пробіл. Спробуйте ще раз')
        continue
