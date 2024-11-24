import random
from typing import List
import classes

def get_random_worker(workers:List[classes.Worker]):
    return random.choice(workers)

def get_random_range(workers:List[classes.Worker]):
    first = random.randint(0, len(workers) - 1)
    second = random.randint(0, len(workers) - 1)
    if first > second: (first, second) = (second, first)
    return workers[first:second]