import random
from typing import List
import re
import classes

def сount_by_name(workers_info:str, name:str):
    return workers_info.lower().count(name.lower())

def get_info_of_workers(workers:List[classes.Worker]):
    info = ""
    for worker in workers:
        info += f"Name: {worker.name}"
        info += f"Age: {worker.age}\n"
    return info

def get_company_info(company:classes.Company, workers:List[classes.Worker]):
    info = (f"Name: {company.name}\n"
             f"Workers count: {len(workers)}\n"
             f"Workers info:\n{get_info_of_workers(workers)}")
    return info

def check_palindrome(name:str):
    middle = len(name) // 2
    if name[0:middle + 1] == name[middle:]:
        return True
    else: return False

def delete_extra_spaces(initially_string):
    new_string = initially_string.strip()
    re.sub(r'\s{2,}', ' ', new_string)
    return len(new_string)

def replace_dots(initially_string:str):
    return initially_string.replace('.', '\n')

def get_random_range(workers_info:str):
    first = random.randint(0, len(workers_info) - 1)
    second = random.randint(0, len(workers_info) - 1)
    if first > second: (first, second) = (second, first)
    return workers_info[first:second]

def get_all_names(workers:List[classes.Worker]):
    names = [w.name for w in workers]
    return " ".join(names)

def check_latin(info:List[str]):
    checked_strings = []
    for string in info:
        count = 0
        words = string.split()
        for word in words:
            if re.search(r'[^a-zA-Z]', word): count += 1
        if count > 0:
            checked_strings.append(string)
    return checked_strings