# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   
# Ввод: 0.01
#     Вывод: 3.14

# import math

# d = float(input("введите точность: "))
# d_len = len(str(d).split('.')[1])
# print(round(math.pi, d_len))


# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# path = r'dz_4.txt'
# with open('path', 'w') as data:
#     data.write('N = ')
#     data.write(input('Введите N: '))
    
# with open('dz_4.txt', 'r+') as data:
#     n = int(data.read().split(' ')[2])
#     data.write('\nProstie mnojiteli chisla N: ')
#     i = 2
#     while n != 1:
#         if(n % i == 0):
#             n /= i
#             data.write(str(i) + '  ')
#             i = 2
#         else: 
#             i += 1

# with open('dz_4.txt', 'r') as data:
#     print(data.readlines()[1])



# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

# my_list = [1, 1, 2, 18, 3, 4, 45, 4, 4]
# my_list = sorted(my_list)
# set_a = set(my_list)
# for i in range(0, len(my_list)-1):
#     if (my_list[i] == my_list[i+1]):
#         set_a.discard(my_list[i])

# print(set_a)
# print(my_list)




# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
# import random

# k = int(input('Введите k: '))

# path = r'dz_4.txt'
# with open('path', 'w') as data:

#     while k >= 0:
#         list[i] = random.randint(0, 100)
#         if list[i] > 0 and k > 1:
#             data.write(str(list[i]) + '(x**'+str(k) + ') + ')
#         elif list[i] > 0 and k == 1:
#             data.write(str(list[i]) + 'x' + ' + ')
#         elif list[i] > 0 and k == 0:
#             data.write(str(list[i]) + ' = 0')
#         elif list[i] == 0 and k == 0:
#             data.write(' = 0')
#         k -= 1


# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов 
# (складываются числа, у которых "х" в одинаковых степенях).

with open('dz_4_5_result.txt', 'w') as data_res:
    with open('dz_4_5_1.txt', 'r') as data_1:
        file1 = data_1.read().replace(' ', '').replace('(','').replace(')','').replace('=','+').split('+')
        
        with open('dz_4_5_2.txt', 'r') as data_2:
            file2 = data_2.read().replace(' ', '').replace('(','').replace(')','').replace('=','+').split('+')
            
            list1 = []
            list2 = []

            for i in file1:
                list1.append(int(i.split('x')[0]))
            for i in file2:
                list2.append(int(i.split('x')[0]))
            
    list1.reverse()
    list2.reverse()
            
    if len(list1) < len(list2): 
        n = len(list1)
        list = list2
    else: 
        n = len(list2)
        list = list1
    i = 0
    while i < n:
        list[i] = list1[i] + list2[i]
        i += 1
            
    list.reverse()
    i = 0
    k = len(list)-2
    while k >= 0:
        if k > 1:
            data_res.write(str(list[i]) + '(x**' + str(k) + ') + ')
        elif k == 1:
            data_res.write(str(list[i]) + 'x' + ' + ')
        elif  k == 0:
            data_res.write(str(list[i]) + ' = 0')
        elif k == 0:
            data_res.write(' = 0')
        k -= 1
        i += 1

print(list)