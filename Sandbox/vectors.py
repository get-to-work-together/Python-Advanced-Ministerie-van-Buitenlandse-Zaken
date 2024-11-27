import math


class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f'[{self._x}, {self._y}]'

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def length(self):
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def __gt__(self, other):
        return self.length() > other.length()
    def __ge__(self, other):
        return self.length() >= other.length()
    def __lt__(self, other):
        return self.length() < other.length()
    def __le__(self, other):
        return self.length() <= other.length()
    def __eq__(self, other):
        return self.length() == other.length()
    def __ne__(self, other):
        return self.length() != other.length()
