# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

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







# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

# # сделано с интелектом))) 
# from tkinter import *
# from tkinter import messagebox as mb

# import random

# root = Tk()
# root.title('Игра с конфетами 1 vs 1')
# root.geometry('400x200+450+250')
# root.resizable(width=False, height=False)

# value = IntVar()
# count = [200]
# count1 = [0]
# count2 = [0]
# c = 1

# def check(v):
#     answer = mb.showinfo(
#         title="Ура!!!", 
#         message= v )

# def test(c):
#     if(c[-1] <= 0):
#         victory = ''
#         if (len(c)%2 == 0):
#             return check('Победил игрок 1')
#         else: 
#             return check('Победил Bot')   

# def game_1vs1():
#     get = value.get()
    
#     if (0 < get < 29):
#         count.append(count[-1] - get)
#         l_count['text'] = count[-1]
#         if (len(count)%2 == 0):
#             count1.append(get)
#             l_player_1['text'] = 'Игрок 1: мои конфеты: \n' + str(sum(count1))
#         else:
#             count2.append(get)
#             l_player_2['text'] = 'Игрок 2: мои конфеты: \n' + str(sum(count2))
            
#         if(count[-1] <= 0):
#             victory =('Победил игрок ' + str(len(count)%2 + 1))
#             check(str(victory))

# def game_1vsbot():
#     get = value.get()
    
#     if (0 < get < 29):
#         # r = random.randint(0, 29)
#         intelect = 0
#         count.append(count[-1] - get)
#         count1.append(get)
#         l_player_1['text'] = 'Игрок 1: мои конфеты: \n' + str(sum(count1))
#         test(count)
#         intelect = count[-1] % 28 - 1
#         if(intelect == -1):
#             intelect = 27
#         elif(intelect == 0):
#             intelect = 28
#         if(0 < count[-1] < 29):
#             intelect = count[-1]
#         count.append(count[-1] - intelect)
#         count2.append(intelect)
#         l_bot['text'] = 'Bot: мои конфеты: \n' + str(sum(count2))
#         l_count['text'] = count[-1]    
        
#         test(count)
           
            
# l = Label(text = 'колличество конфет')
# l_count = Label(text = count[-1])
# l_player_1 = Label(text = 'Игрок 1: мои конфеты: \n' + str(count1[-1]))
# l_player_2 = Label(text = 'Игрок 2: мои конфеты: \n' + str(count2[-1]))
# l_bot = Label(text = 'Bot: мои конфеты: \n' + str(count2[-1]))
# e1 = Entry(textvariable = value)
# b1 = Button(command = game_1vsbot, text = 'взять') # меняем game_1vsbot на game_1vs1 для игры 1 на 1
# btn_info = Message(text="победа")

# # b1.bind('<Button-1>', test)

# l.grid(row=1, column=2)
# l_count.grid(row=2, column=2)
# e1.grid(row=3, column=2)
# b1.grid(row=4, column=2)


# l_player_1.grid(row=5, column=1)
# l_player_2.grid(row=5, column=3)
# l_bot.grid(row=6, column=3)

# root.mainloop()









# Создайте программу для игры в ""Крестики-нолики"".



# pole = list(range(1,10))

# def ris_pole(p):
#    print("-" * 13)
#    for i in range(3):
#       print("|", pole[0+i*3], "|", pole[1+i*3], "|", pole[2+i*3], "|")
#       print("-" * 13)

# while True:
#     ris_pole(pole) 
#     x = int(input('куда поставим Х'))
#     pole[x-1] = 0
#     ris_pole(pole)

     




# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


# def RLE_alg_s(q):
#     count = 1
#     resault = [q[0]]
#     i = 1
#     while i < len(q):
#         if (resault[-1] == q[i]):
#             count += 1
#             if(i == len(q)-1):
#                 resault.insert(-1, str(count))   
#         else:
#             if(count != 1):
#                 resault.insert(-1, str(count))
#                 count = 1
#             resault.append(q[i])
#         i += 1
#     res = ''.join(resault)
#     return res

# def RLE_alg_v(v):
#     res = []
#     for i in range (0, len(v)):
#         # if (int(res[i]) == True):   
#         if (v[i].isdigit() == True):
#             for j in range (0, int(v[i])-1):
#                 res.append(v[i+1])
#         else:
#             res.append(v[i])
#     res_str = ''.join(res)
#     return res_str


# import pathlib
# from pathlib import Path 

# path = Path('seminar 5' ,'file5_1.txt')
# with open (path, 'r+') as data:
#     s = data.readline()
#     data.write('\n' + RLE_alg_s(s))
    
    
# with open (path, 'r+') as data:    
#     data.readline()
#     v = data.readline()
#     data.write('\n' + RLE_alg_v(v))

# Входные и выходные данные хранятся в отдельных текстовых файлах.




