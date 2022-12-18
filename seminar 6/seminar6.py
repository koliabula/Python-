s = input('Введите пример: ')

def my_parse(s):
    s_list = []
    buf = ''
    for i in range(len(s)):
        if (s[i].isdigit()):
            buf += s[i]
        else:
            s_list.append(int(buf))
            s_list.append(s[i])
            buf = ''
    else:
        s_list.append(int(buf))
    return s_list



l_lst = my_parse(s)


while ('*' in l_lst) or ('/' in l_lst):
    mult = -1
    
    if ('*' in l_lst):
        mult = l_lst.index('*')
    
    div = -1
    if ('/' in l_lst):
        div = l_lst.index('/')

    if ((mult < div) and (mult != -1) and (div != -1)) or ((mult != -1) and (div == -1)):
        res = l_lst[mult-1] * l_lst[mult+1]
        l_lst = l_lst[:mult - 1] + [res] + l_lst[mult + 2 :]

    elif ((div < mult) and (div != -1) and (mult != -1)) or ((mult == -1) and (div != -1)):
        res = l_lst[div-1] / l_lst[div+1]
        l_lst = l_lst[:div - 1] + [res] +  l_lst[div + 2 :]

    
while ('+' in l_lst) or ('-' in l_lst):
    plus = -1
    
    if ('+' in l_lst):
        plus = l_lst.index('+')
    
    minus = -1
    if ('-' in l_lst):
        minus = l_lst.index('-')

    if ((plus < minus) and (plus != -1) and (minus != -1)) or ((plus != -1) and (minus == -1)):
        res = l_lst[plus-1] + l_lst[plus+1]
        l_lst = l_lst[:plus - 1] + [res] + l_lst[plus + 2 :]

    elif ((minus < plus) and (minus != -1) and (plus != -1)) or ((plus == -1) and (minus != -1)):
        res = l_lst[minus-1] - l_lst[minus+1]
        l_lst = l_lst[:minus - 1] + [res] +  l_lst[minus + 2 :] 

print(l_lst)