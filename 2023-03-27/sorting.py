from typing import (
    List,
    Any,
)


def bubble_sort(array: List[Any]):
    for top in range(0, len(array) - 1):
        for current in range(0, len(array) - top - 1):
            print(f"{top}.{current}: {array[current]} // {array[current + 1]}")
            print(array)
            if array[current] > array[current + 1]:
                array[current + 1], array[current] = array[current], array[current + 1]
            print(array)

    return array


def selection_sort(array: List[Any]):
    for bottom in range(0, len(array) - 1):
        for current in range(bottom + 1, len(array)):
            print(f"{bottom}.{current}: {array[bottom]} // {array[current]}")
            print(array)
            if array[current] < array[bottom]:
                array[bottom], array[current] = array[current], array[bottom]

            print(array)

    return array


def count_sort(array: List[Any]):
    options = {}
    for item in array:
        if item not in options:
            options[item] = 0

        options[item] += 1

    result = []
    for key in selection_sort(list(options.keys())):
        result.extend([key] * options[key])

    print(result)

    return result


if __name__ == "__main__":
    heroes = ["gandalf", "frodo", "spiderman", "aragorn", "arven"]

    # 1.1 [*"gandalf", *"frodo", "spiderman", "aragorn", "arven"] -> [*"frodo", *"gandalf", "spiderman", "aragorn", "arven"]
    # 1.2 ["frodo", *"gandalf", *"spiderman", "aragorn", "arven"] -> ["frodo", *"gandalf", *"spiderman", "aragorn", "arven"]
    # 1.3 ["frodo", "gandalf", *"spiderman", *"aragorn", "arven"] -> ["frodo", "gandalf", *"aragorn", *"spiderman", "arven"]
    # 1.4 ["frodo", "gandalf", "aragorn", *"spiderman", *"arven"] -> ["frodo", "gandalf", "aragorn", *"arven", *"spiderman"]
    # 2.1 [*"frodo", *"gandalf", "aragorn", "arven", "spiderman"] -> [*"frodo", *"gandalf", "aragorn", "arven", "spiderman"]
    # 2.2 ["frodo", *"gandalf", *"aragorn", "arven", "spiderman"] -> ["frodo", *"aragorn", *"gandalf", "arven", "spiderman"]
    # 2.3 ["frodo", "aragorn", *"gandalf", *"arven", "spiderman"] -> ["frodo", "aragorn", *"arven", *"gandalf", "spiderman"]
    # 3.1 [*"frodo", *"aragorn", "arven", "gandalf", "spiderman"] -> [*"aragorn", *"frodo", "arven", "gandalf", "spiderman"]
    # 3.2 ["aragorn", *"frodo", *"arven", "gandalf", "spiderman"] -> ["aragorn", *"arven", *"frodo", "gandalf", "spiderman"]
    # 4.1 [*"aragorn", *"arven", "frodo", "gandalf", "spiderman"] -> [*"aragorn", *"arven", "frodo", "gandalf", "spiderman"]

    print("BUBBLE")
    assert bubble_sort(heroes) == ["aragorn", "arven", "frodo", "gandalf", "spiderman"]

    print("SELECTION")
    assert selection_sort(heroes) == ["aragorn", "arven", "frodo", "gandalf", "spiderman"]

    print("COUNT")
    assert count_sort(heroes) == ["aragorn", "arven", "frodo", "gandalf", "spiderman"]
