'''       Задача 10:
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
'''
from random import randint
n = int(input('Введите количество монеток: '))
side1, side2, i = 0, 0, 0
count_side1, count_side2 = 0, 0

# стороны монет: 
# count_side1 - решко 
# count_side2 - герб
while i < n:
    side1, side2 = randint(0, 1), randint(0, 1)
    if side1 > 0:
        count_side1 += 1
    else:
        count_side2 += 1
    i += 1
print(count_side1, count_side2)

if count_side2 > count_side1:
    print(f'{count_side1} монеток нужно перевернуть')
else:
    print(f'{count_side2} монеток нужно перевернуть')


