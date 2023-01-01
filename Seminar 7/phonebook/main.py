import controller as c
import view as v

while True:
    n = v.choice()
    if n == 1:
        c.view_numbers()
    elif n == 2:
        c.search_number()
    elif n == 3:
        c.add_number()
    elif n == 4:
        c.change_number()
    elif n == 5:
        c.delete_number()

    elif n == 6:
        break