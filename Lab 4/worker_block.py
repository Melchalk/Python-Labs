import company_classes as company
import exceptions as ex

def create_worker(name, age):
    if age < 18:
        raise ex.ArgumentException("Age is too small")
    return company.Worker(name, age)

def try_get_worker(name):
    try:
        worker = [x for x in company.Company.workers if x.name == name]
        if len(worker) == 0: raise ex.NotFound("Worker was not found")
        return worker
    except ex.NotFound:
        return False

def update_workers_age(name, new_age):
    response = True
    try:
        if len(name) <= 0 or name is None:
            raise ex.NullOrEmptyException("Name can not be empty")
        worker = [x for x in company.Company.workers if x.name == name]
        if len(worker) == 0:
            raise ex.NotFound("Worker was not found")
        worker[0].age = new_age
    except ex.NullOrEmptyException:
        response = False
    except ex.NotFound:
        response = False
    except Exception:
        response = False
    finally:
        return response

def dismiss_worker(name):
    response = True
    try:
        if len(name) <= 0 or name is None:
            raise ex.NullOrEmptyException("Name can not be empty")
        worker = [x for x in company.Company.workers if x.name == name]
        if len(worker) == 0:
            raise ex.NotFound("Worker was not found")
        company.Company.workers.remove(worker)
    except ex.NullOrEmptyException:
        response = False
    except ex.NotFound:
        response = False
    except Exception:
        response = False
    finally:
        return response