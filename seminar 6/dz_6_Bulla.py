# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной идексах.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

# ТАК БЫЛО
# spisok = [2, 3, 5, 9, 3]
# def my_sum(s):
#     sum_ = 0
#     for i in range(1, len(s), 2):
#         sum_ += s[i]
#     return sum_
# print(my_sum(spisok))


# ТАК СТАЛО
# spisok = [2, 3, 5, 9, 3]
# sum_ = [spisok[i] for i in range(1, len(spisok), 2)]
# print(sum(sum_))







# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# ТАК БЫЛО
# import math
# spisok = [2, 3, 4, 5, 6]
# def my_proizv(s):
#     proizv_ = []
#     for i in range(0, math.ceil(len(s)/2)):
#         proizv_.append(s[i] * s[-i-1])
#     return proizv_

# print(my_proizv(spisok))

# ТАК СТАЛО
# import math
# spisok = [2, 3, 4, 5, 6]
# proizv_ = [spisok[i] * spisok[-i-1] for i in range(0, math.ceil(len(spisok)/2))]
# print(proizv_)


# Считать строку из набора чисел из файла. 
# Напишите программу которая покажет MAX и MIN число.
# В качестве разделителей используйте пробел.
# Результат записать в конец исходного файла.


# import pathlib
# from pathlib import Path 

# path = Path('seminar 6' ,'fileS4.txt')
# with open(path, 'w') as data:
#     data.write(input('Введите цифры через пробел: ' ))
# ТАК БЫЛО
# with open(path, 'r+') as data:
    # s = ''
    # for i in data:
    #     s = i.split(' ')

    # list = []
    # for i in s:
    #     list.append(int(i))

    # max_min = max(list), min(list)
    # data.write('\n')
    # data.write(str(max_min))

# ТАК СТАЛО
# with open(path, 'r+') as data:
#     s = data.read().split(' ')
#     list = [i for i in s]
#     max_min = max(list), min(list)
#     data.write('\n')
#     data.write(str(max_min))




# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# import math
# number2 = int(input('Введите число:==> '))

# ТАК БЫЛО
# i = 1
# while i <= number2:
#     print(math.factorial(i), end = ' ')
#     i += 1

# ТАК СТАЛО
# import math
# number2 = int(input('Введите число:==> '))
# print(list(map(math.factorial, range(1, number2+1))))