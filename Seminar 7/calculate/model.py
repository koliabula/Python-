
def calculate(s_l):    
    while ('*' in s_l) or ('/' in s_l):
        mult = -1
        
        if ('*' in s_l):
            mult = s_l.index('*')
        
        div = -1
        if ('/' in s_l):
            div = s_l.index('/')

        if ((mult < div) and (mult != -1) and (div != -1)) or ((mult != -1) and (div == -1)):
            res = s_l[mult-1] * s_l[mult+1]
            s_l = s_l[:mult - 1] + [res] + s_l[mult + 2 :]

        elif ((div < mult) and (div != -1) and (mult != -1)) or ((mult == -1) and (div != -1)):
            res = s_l[div-1] / s_l[div+1]
            s_l = s_l[:div - 1] + [res] +  s_l[div + 2 :]

    while ('+' in s_l) or ('-' in s_l):
        plus = -1
        
        if ('+' in s_l):
            plus = s_l.index('+')
        
        minus = -1
        if ('-' in s_l):
            minus = s_l.index('-')

        if ((plus < minus) and (plus != -1) and (minus != -1)) or ((plus != -1) and (minus == -1)):
            res = s_l[plus-1] + s_l[plus+1]
            s_l = s_l[:plus - 1] + [res] + s_l[plus + 2 :]

        elif ((minus < plus) and (minus != -1) and (plus != -1)) or ((plus == -1) and (minus != -1)):
            res = s_l[minus-1] - s_l[minus+1]
            s_l = s_l[:minus - 1] + [res] +  s_l[minus + 2 :] 

    return s_l

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