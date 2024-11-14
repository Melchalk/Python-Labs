from typing import List

import company_classes as company
import exceptions as ex

def create_company(name):
    if len(name) <= 0 or name is None:
        raise ex.NullOrEmptyException("Name can not be empty")
    return company.Company(name)

def average_salary(workers:List[company.Worker]):
    try:
        salary = 0
        for worker in workers:
            salary += worker.salary
        return salary / len(workers)
    except ex.NullOrEmptyException:
        return "Some workers dont have salary yet"
    except ZeroDivisionError:
        return "Workers count was zero"
    except Exception as e:
        return "Something was incorrect"

def get_info_of_workers(workers:List[company.Worker]):
    response = ""
    try:
        info = ""
        for worker in workers:
            info += "------------\n"
            info += f"Name: {worker.name}"
            info += f"Age: {worker.age}"
            info += f"Salary: {worker.salary}"
        response = info
    except ex.NullOrEmptyException:
        response = "Some workers dont have salary yet"
    except Exception as e:
        response = "Something was incorrect"
    finally:
        return f"Result: {response}"

def get_company_info():
    response = ""
    try:
        info = ""
        info += f"Name: {company.Company.name}"
        info += f"Workers count: {len(company.Company.workers)}"
        info += "Workers info:"
        info += get_info_of_workers(company.Company.workers)

        response = info
    except Exception as e:
        response = e
    finally:
        return response