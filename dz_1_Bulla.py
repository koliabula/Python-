# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# number = int(input('Введите цифру, обозначающую день недели:-->'))
# if number > 0 and number <= 7:
#     if number > 5:
#         print('Сегодня Выходной')
#     else: 
#         print('Сегодня НЕ Выходной')
# else:
#     print('Такого дня недели нет')


# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. ⋀ - and ⋁ - or ¬ - not
    
# for x in range(1, 3):
#     for y in range(1, 3):
#         for z in range(1, 3):
#             help = not(x or y or z) == (not x) and (not y) and (not z)
#             print('¬(', x,' ⋁ ', y, ' ⋁ ', z,') = ¬', x,  '⋀ ¬', y, ' ⋀ ¬', z, ' --> ', help)

            

# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


# print('Введите координаты точки:')
# x = int(input('x --> '))
# y = int(input('y --> '))

# if x > 0 and y > 0:
#     print('Четверть 1')

# elif x < 0 and y > 0:
#     print('Четверть 2')

# elif x < 0 and y < 0:
#     print('Четверть 3')

# elif x > 0 and y < 0:
#     print('Четверть 4')
# else:
#     print('error')


# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# number = int(input('Введите номер четверти: --> '))
    
# if number == 1:
#     print('x = (0; + inf)    y = (0; + inf)')

# elif number == 2:
#     print('x = (0; + inf)    y = (- inf; 0)')

# elif number == 3:
#     print('x = (- inf; 0)    y = (- inf; 0)')

# elif number == 3:
#     print('x = (- inf; 0)    y = (0; + inf)')

# else: print ('error')

# import math
# from math import hypot

# x1 = int(input('x1 --> '))
# y1 = int(input('y1 --> '))
# x2 = int(input('x2 --> '))
# y2 = int(input('y2 --> '))
 
# print(hypot(x2-x1, y2-y1))