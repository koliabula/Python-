# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

# number = float(input('Введите вещественное число:==> '))
# n = str(number)

# lef, righ = n.split('.')
# lefrigh = lef + righ
# n_lefrigh = int(lefrigh)

# summa = 0
# while n_lefrigh > 0:
#     summa += n_lefrigh % 10
#     n_lefrigh //= 10

# print('Сумма цифр вещественного числа: --> ', summa)




# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# import math
# number2 = int(input('Введите число:==> '))

# i = 1
# while i <= number2:
#     print(math.factorial(i), end = ' ')
#     i += 1




# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

# number3 = int(input('Введите n:==> '))

# dictionary = {i: (1+1/i)**i for i in range(1, number3+1)}

# print(dictionary)

# summa = 0
# for k in dictionary.values():
#     summa += k

# print('Сумма: --> ', summa)




# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

# number4 = int(input('Задайте Длинну Списка:==> '))

# spis = []
# for i in range(-number4, number4 + 1):
#     spis.append(i) 
# print(spis)

# index = input('Введите индексы: --> ')
# s = index.split(' ')
# s_index = []

# for i in range(0, len(s)):
#     s_index.append(int(s[i])) 

# pr = 1
# for i in range(0, len(s_index)):
#     print(spis[s_index[i]], end = ' ') 
#     pr *= spis[s_index[i]]
# print('Произведение = ', pr)




# Реализуйте алгоритм перемешивания списка.
import random

spis2 = [1, 2, 3, 4, 5]

random.shuffle(spis2)

print(spis2)