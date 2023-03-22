from typing import Any

storage = [None for _ in range(100)]


def hash_func(key: str):
    total = 0
    for char in key:
        total += ord(char)

    return total % 100


def add(key: str, value: Any):
    hashed = hash_func(key)
    storage[hashed] = value


def get(key: str):
    hashed = hash_func(key)
    return storage[hashed]


if __name__ == "__main__":
    # print(hash_func("gandalf_the_gray"))
    add("a", 1)
    add("abc", 3)
    add("gandalf_the_gray", 99)
    print(storage)

    print(get("gandalf_the_gray"))
    print(hash_func("gandalf_not_the_gray"))
    print(get("gandalf_not_the_grcy"))
