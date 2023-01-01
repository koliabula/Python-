


            
def view_phonebook(d_f):
    for s in d_f:
        print(str(s))
    input('нажмите enter...')


def choice():
    print('-----ТЕЛЕФОННЫЙ СПРАВОЧНИК----')
    print('1 - Просмотреть справочник')
    print('2 - Найти контакт')
    print('3 - Добавить контакт')
    print('4 - Редактировать контакт')
    print('5 - Удалить контакт')
    print('\n 6 - Закрыть справочник')
    choice = int(input('Введите номер операции: '))
    return choice

