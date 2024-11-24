import math
import classes
import decimal_funcs as df
import locate_funcs as lf
from typing import List

def get_younger_worker(*workers):
    ages = [w.age for w in workers]
    min_age = min(ages)
    for item in workers:
        if item.age == min_age:
            return item.name

def get_comb_k_workers(workers:List[classes.Worker], k:int):
    return math.comb(len(workers), k)

def get_average_salary(statistics:List[classes.WorkersStatistic]):
    total = math.fsum([s.salary for s in statistics])
    round_salary = df.round_average_salary(total / len(statistics))
    return lf.get_locate_salary(round_salary)