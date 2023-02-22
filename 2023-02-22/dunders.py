from typing import Callable
from functools import wraps


def print_func(func: Callable):
    @wraps(func)
    def wrap(*args, **kwargs):
        print(func.__name__)

        return func(*args, **kwargs)

    return wrap


# @print_func
def hello_world():
    print("Hello World")


# dec_f = print_func(hello_world)
# dec_f()

# hello_world()


class PrintDecorator:

    def __init__(self, func: Callable):
        self.func = func  # TODO: use wraps
        # print(self.func)
        # print("__init__")

    def __call__(self, *args, **kwargs):
        # print(self.func.__name__)
        print("__call__")
        return self.func(*args, **kwargs)


@PrintDecorator
def hello_world():
    """docsting"""
    print("Hello World")


# hello_world()
# print(hello_world.__doc__ == "docsting")
# dec = PrintDecorator(hello_world)
# print(dec, type(dec))
# dec()

# hello_world()


class Wizard:

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __call__(self, *args, **kwargs):
        print(f"{self} called with args={args}, kwargs={kwargs}")


# gendalf = Wizard("Gendalf")
# gendalf()
# gendalf(1, 2, k=1)


class Number:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value}"

    def __add__(self, other) -> "Number":
        if isinstance(other, Number):
            return Number(self.value + other.value)

        if isinstance(other, (int, float)):
            return Number(self.value + other)

        raise TypeError()

    def __eq__(self, other):
        if isinstance(other, Number):
            return self.value == other.value

        if isinstance(other, (int, float)):
            return self.value == other

        return False


one = Number(1)
two = Number(2)

# print(one, two)
# print(one + two)
# print(type(one + two))
#
result = two + Number(0)
# print(result)

assert str(one + two) == str(3)
assert two == result, f"{two} != {result}"
assert two == 2, f"{two} != {2}"
assert two == 2.0, f"{two} != {2.0}"


class Dictionary:

    def __init__(self):
        print("Constructor")
        self._value = {
            "123": 800,
        }
        self.file = open("./dunders.py")

    def __getitem__(self, item):
        if item not in self._value:
            raise KeyError(item)

        return self._value[item]

    def __setitem__(self, key, value):
        self._value[key] = value

    def __delitem__(self, key):
        del self._value[key]

    def __contains__(self, item):
        return item in self._value

    def __del__(self):
        print("Destructor")
        if not self.file.closed:
            self.file.close()


d = Dictionary()
d["1230"] = "Gendalf"
del d["1230"]
print("1230" in d)

del d

print(123123)
