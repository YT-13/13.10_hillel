# 2 Програма повинна вивести трикутник як на малюнку.
# Програма отримує число - скільки вивести рядків.
# Кожен рядок має номер та число вирівняне по правому краю з кількистю нулів відповіно до номера рядку.

x = '0'
y = '1'
input_number = int(input('введіть число >>> '))
len_number = len(str(input_number))
for elen in range(0, input_number + 1):
    k = y + x * elen
    print('{:>{}} {:>{}}'.format(elen, len_number, k, input_number +1))
