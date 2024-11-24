from array import ArrayType

def check_age(*person):
    name, age = person
    if age < 18: return False
    return True

def get_types(*args):
    types = tuple()
    for item in args:
        types += (type(item),)
    return types

def check_availability_item(*args, element):
    for item in args:
        if item == element:
            return True
    return False

def count_key(base_list:ArrayType, key):
    count = 0
    for dict in base_list:
        if key in dict: count += 1
    return count

def try_get_value(base_dict, key):
    try:
        base_dict[key]
    except KeyError:
        print("Nope!")