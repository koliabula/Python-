import model
import view


def button_click():
    global value_s
    value_s = view.get_value()
    result = model.calculate(model.my_parse(value_s))
    view.view_data(result)