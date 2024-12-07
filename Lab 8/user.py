from dataclasses import dataclass

@dataclass
class User:
    id: int
    username: str
    email : str
    password: str


users = [User(1, "Mel", "mail", "123"), User(2, "Max", "mail", "123")]