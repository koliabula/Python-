# Считать строку из набора чисел из файла. 
# Напишите программу которая покажет MAX и MIN число.
# В качестве разделителей используйте пробел.
# Результат записать в конец исходного файла.

# p = r'fileS4.txt'
# with open(p, 'w') as data:
#     data.write(input('Введите цифры через пробел: ' ))

# with open(p, 'r+') as data:
#     s = ''
#     for i in data:
#         s = i.split(' ')

#     list = []
#     for i in s:
#         list.append(int(i))

#     max_min = max(list), min(list)
#     data.write('\n')
#     data.write(str(max_min))



# Найти корни квадратного уравнения ax2 + bx + c = 0 двумя споcобами (получить кортеж)

# 1) с помощью мат формул
# 2) с помощью бибдиатек Python

# D = b2 − 4ac 

def my_func(a, b, c):
    
    d = b**2 - 4 * a * c

    if d < 0: return print('Нет корней')

    elif d == 0: 
        x = -b / 2 * a
        return x
    elif d > 0:
        t = ((-b + d**0.5) / (2 * a), (-b - d**0.5) / (2 * a))
        return t 

a = int(input('A: '))
b = int(input('B: '))
c = int(input('С: '))

print(my_func(a, b, c))

