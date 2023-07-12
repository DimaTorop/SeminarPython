'''         Задача 8: 
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
'''

chocolate_length = int(input('Введите длину шоколадки: '))
chocolate_width = int(input('Введите ширину шоколадки: '))
break_slice = int(input('Сколько отломить долек: '))

if(((chocolate_length * chocolate_width) - break_slice) % 2 == 0):
    print(f'{chocolate_length} {chocolate_width} {break_slice} -> yes')
else:
    print(f'{chocolate_length} {chocolate_width} {break_slice} -> no')
