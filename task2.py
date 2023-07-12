'''     Задача 2:
Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 
'''

three_digit_number = int(input('Введите трёхзначное число: '))

#    three_digit_number // 100                # сотни
#    three_digit_number // 10 % 10            # дестки
#    three_digit_number % 10                  # единицы

if(three_digit_number >= 100 and three_digit_number <= 999):
    hundreds = three_digit_number // 100
    dozens = three_digit_number // 10 % 10
    units = three_digit_number % 10
    res = hundreds + dozens + units
    print(f'{three_digit_number} -> {res} ({hundreds} + {dozens} + {units})')   
elif(three_digit_number > 999, three_digit_number < 99):
    print('Введите трехзначное число')