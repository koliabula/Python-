import model
import view

def button_click():
    value_s = view.get_value()

    model.init(value_s)
    result = model.calculate(model.init(value_s))
    view.view_data(result)