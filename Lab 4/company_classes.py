from typing import List

class Worker:
    salary: int | None
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    name: str
    workers: List[Worker]
    def __init__(self, name):
        self.name = name