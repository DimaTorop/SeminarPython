"""                      Задача 6:
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
которая проверяет счастливость билета.
*Пример:*

385916 -> yes
123456 -> no
"""

number_ticket = int(input("Введите номер биета:"))
sum1 = 0
sum2 = 0


if (number_ticket >= 100000 and number_ticket <= 999999):
    first = number_ticket // 100000
    second = number_ticket // 10000 % 10
    third = number_ticket // 1000 % 10
    fourth = number_ticket // 100 % 10
    fifth = number_ticket // 10 % 10
    sixth = number_ticket % 10
    sum1 = first + second + third
    sum2 = fourth + fifth + sixth
    if (sum1 == sum2):
        print(f"{number_ticket} -> yes")
    else:
        print(f"{number_ticket} -> no")
else: 
    print(f"Введено неверное число!!!")
