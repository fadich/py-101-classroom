from typing import Sequence, Any

a = "o"

name = "joe"


def funct():
    user = get_user_from()
    if user:
        update_status(user)
        return

    print("user not found")
    ...
    ...


# var = funct()
# print(var)


def count_chars(n: Sequence[Any]) -> str:
    return f"{len(n)}"


count_chars([])

print(name)
