
list_data = [1*8-9/45] 

def init(l):
    global list_data 
    list_data = my_parse(l) 



def calculate():    
    while ('*' in list_data) or ('/' in list_data):
        mult = -1
        
        if ('*' in list_data):
            mult = list_data.index('*')
        
        div = -1
        if ('/' in list_data):
            div = list_data.index('/')

        if ((mult < div) and (mult != -1) and (div != -1)) or ((mult != -1) and (div == -1)):
            res = list_data[mult-1] * list_data[mult+1]
            list_data = list_data[:mult - 1] + [res] + list_data[mult + 2 :]

        elif ((div < mult) and (div != -1) and (mult != -1)) or ((mult == -1) and (div != -1)):
            res = list_data[div-1] / list_data[div+1]
            list_data = list_data[:div - 1] + [res] +  list_data[div + 2 :]

    while ('+' in list_data) or ('-' in list_data):
        plus = -1
        
        if ('+' in list_data):
            plus = list_data.index('+')
        
        minus = -1
        if ('-' in list_data):
            minus = list_data.index('-')

        if ((plus < minus) and (plus != -1) and (minus != -1)) or ((plus != -1) and (minus == -1)):
            res = list_data[plus-1] + list_data[plus+1]
            list_data = list_data[:plus - 1] + [res] + list_data[plus + 2 :]

        elif ((minus < plus) and (minus != -1) and (plus != -1)) or ((plus == -1) and (minus != -1)):
            res = list_data[minus-1] - list_data[minus+1]
            list_data = list_data[:minus - 1] + [res] +  list_data[minus + 2 :] 

    return list_data

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