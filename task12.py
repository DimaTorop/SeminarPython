'''              Задача 12:
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
'''
from random import randint
x, y = randint(1, 1000), randint(1, 1000)
print(x, y)
s = x + y
p = x * y
print(s, p)
c = s // 2
f = (s / 2) + c
print(c, f)