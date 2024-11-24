from array import ArrayType
from random import randint

def reverse_list(base_list:ArrayType):
    new_list = []
    for i in range(len(base_list) - 1, -1, -1):
        new_list.append(base_list[i])
    return new_list

def compare_lists(first:ArrayType, second:ArrayType):
    if first != second: return False
    for i in range(len(first)):
        if first[i] != second[i]: return False
    return True

def get_range(base_list:ArrayType, first_index, second_index):
    if first_index < 0 or first_index >= len(base_list):
        first_index = 0
    if second_index < 0 or second_index >= len(base_list):
        second_index = len(base_list) - 1
    return base_list[first_index:second_index]

def new_list_by_arithmetic_progression(first_item, count, difference):
    new_list = [first_item]
    while len(new_list) != count:
        new_list.append(new_list[-1] + difference)
    return new_list

def insert_an_element(base_list:ArrayType, index, item):
    return base_list[0:index] + [item] + base_list[index:len(base_list)]

def join_and_sort_list(first:ArrayType, second:ArrayType, by_ascending:True):
    new_list = first + second
    return sorted(new_list, reverse=by_ascending)

def generate_list():
    new_list = new_list_by_arithmetic_progression(
        randint(1, 10), randint(1, 10), randint(1, 10))
    while len(new_list) % 2 == 0:
        new_list = new_list_by_arithmetic_progression(
            randint(1, 10), randint(1, 10), randint(1, 10))
    median = new_list[(len(new_list) + 1)//2]
    return new_list.count(median)

def delete_min(base_list:ArrayType):
    min_item = min(base_list)
    base_list.remove(min_item)
    return min_item

def get_two_dimensional_list(base_list:ArrayType):
    new_list = [[],[]]
    for item in base_list:
        if item % 2 == 0: new_list[0].append(item)
        else: new_list[1].append(item)
    return new_list