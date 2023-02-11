import os.path

from functools import wraps

from decors import count_time


ADMIN_PASSWORD = "123"


def admin_access(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if input("PASSWORD: ") != ADMIN_PASSWORD:
            raise PermissionError("Forbidden")

        return func(*args, **kwargs)

    return wrapper


@admin_access
@count_time
def get_file_content(filepath: str):
    with open(filepath, "r") as file:
        return file.read()


@count_time
def get_file_abs_path(filepath: str):
    return os.path.abspath(filepath)


@admin_access
@count_time
def get_file_lines_count(filepath: str):
    with open(filepath) as file:
        return len(file.readlines())


while True:
    menu = {
        "1": get_file_content,
        "2": get_file_abs_path,
        "3": get_file_lines_count,
    }

    for num, f in menu.items():
        print(f"{num}. {f.__name__}")

    item = input(">>> ")
    if item not in menu:
        print("Invalid menu item")
        continue

    item = input("filepath: ")

    try:
        content = get_file_content(item)
    except PermissionError:
        print("NOT PERMITTED")
    else:
        print(content)
