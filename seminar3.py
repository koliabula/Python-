# n = int(input('введите max число: '))

# def my_rand(my_max = 10):
#     import time
    
#     sec = time.time()
#     secstr = str(sec).split('.')
#     ran = int(secstr[1])%my_max
#     return ran


# print(my_rand(n))

# задайте список, напишите программу которая определит, 
# присутствует ли в заданном списке строк некое число

# spis = ['qwe48', 'rty6', 'qwe47', 'qwerty18', 'qwe48', 'rty']
# number = int(input('введите число для поиска: '))

# def poisk_number_to_list(s:list , n:int):
#     nu = str(n)
#     shet = -1
#     for i in s:
#         help = i.split(nu)
#         if i != help[0]:
#             print(i, end = ' ')
#             shet += 1
#     if shet == -1:
#         print('не встречается')

# poisk_number_to_list(spis, number)


# Напишите программу, которая определит позицию второго вхождения строки в списке, 
# либо сообщит, что её нет

# spis = ['qwe48', 'rty6', 'qwe47', 'qwerty18', 'qwe48', 'rty']
# element = input('введите строку для поиска: ')

# def poisk_elem_to_list(s:list , el:str):
#     shet = 0
#     pos = -1
#     i = 0
#     for k in s:
#         if k == el: 
#             shet += 1
#             if shet == 2:
#                 pos = i
#                 print('позиция второго вхождения', el, 'в списке = ', i)
#                 break
#         i += 1
#     if pos == -1:
#         print('не встречается')

# # но можно сделать проще
# def poisk_elem_to_list2(s:list , el:str):
#     n = s.index(el, s.index(el)+1, len(s)+1)     
#     print(n)

# poisk_elem_to_list(spis, element)
# poisk_elem_to_list2(spis, element)
