# Напишите программу, удаляющую из текста все слова, содержищие "абв"

# import pathlib
# from pathlib import Path 

# path = Path('seminar 5' ,'file5.txt')
# with open (path, 'w', encoding="utf-8") as data:
#     data.write('Я люблю кофеабв иабв чай')

# with open (path, 'r+', encoding="utf-8") as data:
#     lst = data.read().split(' ')
#     # lst = [i for i in lst if ('абв' not in i)] #реш 1
#     lst = filter(lambda x: 'абв' not in x, lst) #реш 2
#     data.write('\n' + ' '.join(lst))


# В файле находится N натуральных чисел записанных через пробел
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]
# Найдите это число
    

# n = [i for i in range(5, 11)]
# n.remove(n[4])
# print(n)
# s = [n[i]-1 for i in range(1, len(n)) if (n[i] - 1 != n[i-1])]
# print(s)

# Дан список чисел, создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Поядок элементов менять нельзя.

# import random

# lst = [random.randint(0, 100) for i in range(0, 10)]
# print(lst)
# lst_1 = [lst [0]]
# for i in range(0, len(lst)):
#     if  (max(lst_1) < lst[i]):
#         lst_1.append(lst[i])
# print(lst_1)
