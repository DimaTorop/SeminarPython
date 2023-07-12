'''          Задача 14:
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.'''

num = int(input('Введите число: '))
i, result = 0, 0
while result < num:
    result = pow(2, i)
    i += 1
    print(result, end= '  ')
    
