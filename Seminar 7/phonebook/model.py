
import view
import model as m

# import pathlib
# from pathlib import Path

# path = Path('seminar 7', 'phonebook', 'file' ,'phonebook.txt')
# path2 = Path('seminar 7', 'phonebook', 'file' ,'phonebook1.txt')

def input_data(p):
    with open (p, 'a', encoding="utf-8") as data:
        data.write(input('Имя => ') + '\n' )
        data.write(input('Фамилия => ') + '\n')
        data.write(input('Номер => ') + '\n')
        data.write('!')
        input('Контакт добавлен! нажмите enter...')

def read_phonebook(p):
    with open (p, 'r', encoding="utf-8") as data:
        s = data.read().replace('\n', ' ').split('!')
        del s[-1]
    return s

def search_phones(phone_n):
    search_contact = input('введите имя, фамилию или номер телефона: ')
    list_search = []
    for s in phone_n:
        if search_contact.lower() in s.lower():
            list_search.append(s)
    if len(list_search):
        return list_search
    else: 
        input('Такого контакта нет! жми enter...')
        return 0

def delete_phones(d_f, phone_n, say):
    if len(phone_n) == 1:
        print
        question = input(f'вы точно хотите {say} контакт {phone_n[0]} ?  => ')
        if question.lower() == 'да':
            d_f.remove(phone_n[0])
            input(f'готово, нажмите enter...')
        else:
            input('передумал))), нажмите enter...')
        
        return d_f
    
    if len(phone_n) > 1:
        while True:
            print(phone_n)
            question = int(input(f'Введите номер контакта, который хотите удалить \n от 1 до {len(phone_n)}: '))
            if 1 <= question <= len(phone_n):
                d_f.remove(phone_n[question - 1])
                input('контакт удалён, нажмите enter...')
                break
            else: input('некоректный ввод, попробуем ещё раз, нажмите enter...')
        return d_f

def overwriting(p, list_data):
    with open (p, 'w', encoding="utf-8") as data:
        for i in list_data:
            s = str(i.replace(' ', '\n')) + '!'
            data.write(s)
