import view
import model as m

import pathlib
from pathlib import Path

path = Path('seminar 7', 'phonebook', 'file' ,'phonebook.txt')
path2 = Path('seminar 7', 'phonebook', 'file' ,'phonebook1.txt')

def view_numbers():
    data_phone = m.read_phonebook(path)
    view.view_phonebook(data_phone)

def add_number():
    m.input_data(path)
    
def search_number():
    data_phone = m.read_phonebook(path)
    serch_phone = m.search_phones(data_phone)
    view.view_phonebook(serch_phone)

def delete_number():
    data_phone = m.read_phonebook(path)
    search_phone = m.search_phones(data_phone)
    new_list = m.delete_phones(data_phone, search_phone, 'удалить')
    m.overwriting(path2, new_list)


def change_number():
    data_phone = m.read_phonebook(path)
    search_phone = m.search_phones(data_phone)
    new_list = m.delete_phones(data_phone, search_phone, 'изменить')
    m.overwriting(path, new_list)
    m.input_data(path)
