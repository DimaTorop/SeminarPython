'''
Задача 28: 
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2
    4 
'''

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
result = 0

def subtraction(a, b, result):
    result = a - b
    return result

print(subtraction(a, b, result))


def addition(a, b, result):
    result = a + b
    return result

print(addition(a, b, result))




