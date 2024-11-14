class NotFound(Exception):
    def __init__(self, value):
        self.value = value

class NullOrEmptyException(Exception):
    def __init__(self, value):
        self.value = value

class ArgumentException(Exception):
    def __init__(self, value):
        self.value = value