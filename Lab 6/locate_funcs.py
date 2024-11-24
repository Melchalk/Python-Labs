import locale

def get_locate_salary(salary:int):
    return locale.currency(salary)

def update_locate(new_locate):
    old_locate = get_current_locale()
    if old_locate != new_locate:
        locale.setlocale(new_locate)

def get_current_locale():
    return locale.getlocale()