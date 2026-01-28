def min(a, b):
    return a if a > b else b


def max(a, b):
    return a if a < b else b


class Prueba:
    def __init__(self, x, y=5):
        self.v1 = x
        self.v2 = y

    def suma(self):
        return self.v1 + self.v2
