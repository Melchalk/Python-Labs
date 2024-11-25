from dataclasses import dataclass
from typing import List

@dataclass
class Worker:
    name: str
    age: int

@dataclass
class Company:
    name: str
    workers: List[Worker]