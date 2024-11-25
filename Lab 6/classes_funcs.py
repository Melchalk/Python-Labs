from typing import List
import classes

def create_worker(name, age):
    if age < 18:
        raise Exception("Age is too small")
    new_worker = classes.Worker(name, age)
    return new_worker

def add_worker(worker:classes.Worker):
    if worker.age < 18:
        raise Exception("Age is too small")
    if len(worker.name) == 0 or worker.name is None:
        raise Exception("Name can not be empty")
    return True

def get_ages_by_names():
    dict = {}
    workers = classes.Company.workers
    for worker in workers:
        dict[worker.name] = worker.age
    return dict

def get_info_of_workers(workers:List[classes.Worker]):
    response = ""
    try:
        info = ""
        for worker in workers:
            info += "------------\n"
            info += f"Name: {worker.name}"
            info += f"Age: {worker.age}"
        response = info
    except Exception as e:
        response = "Something was incorrect"
    finally:
        return f"Result: {response}"

def update_workers_age(name, new_age):
    response = True
    try:
        if len(name) <= 0 or name is None:
            raise Exception("Name can not be empty")
        worker = [x for x in classes.Company.workers if x.name == name]
        if len(worker) == 0:
            raise Exception("Worker was not found")
        worker[0].age = new_age
    except Exception:
        response = False
    finally:
        return response