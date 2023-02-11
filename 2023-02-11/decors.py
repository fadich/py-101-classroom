import time

from functools import wraps
from typing import Callable, Dict


def count_time(func: Callable):
    @wraps(func)
    def wrap(*args, **kwargs):
        start_time = time.time()

        value = func(*args, **kwargs)

        end_time = time.time()
        print(f"{func.__name__} took {(end_time - start_time) * 1000:.2f}ms")

        return value

    return wrap


# print_name = count_time(print_name)
@count_time
def print_name(u: Dict[str, str]):
    print(f"USERNAME: {u.get('username')}")


# read_username = count_time(read_username)
@count_time
def read_username() -> str:
    """
    Reads username from terminal

    :return: Given username or '<Anonymous>'
    """

    return input(">>> ") or "<Anonymous>"


if __name__ == "__main__":
    print(read_username.__doc__)

    username = read_username()
    user = {
        "username": username
    }

    print_name(user)
