# Завдання 5
#
# Створіть словник з рядка 'python is good language to code' наступним чином:
# як ключі візьміть літери рядка, а значеннями нехай будуть числа, що відповідають кількості входження даної літери в рядок.

string = 'python is good language to code'
# print(sorted("This is a test string from Andrew".split(), key=str.lower))
# string_set = set(string)
# string = string.split()
string = string.replace(' ', '')

list_string = []
for x in string:
    list_string.append(x)

count_string = []
for i in range(0, len(string)):
    count_string.append(string.count(string[i]))

new_dict = {}
for x, y in zip(string, count_string):
    new_dict[x] = y

print(new_dict)

# print(len(string), len(count_string))

# new_dict = dict(zip(string, count_string))
# print('Отриманий словник:\n', new_dict)