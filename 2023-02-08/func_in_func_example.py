
def circle_area(pi, world_name: str):
    count_calls = 0

    def count_area(r):
        nonlocal count_calls

        count_calls += 1
        print(f"Called in {world_name} world {count_calls} times")

        return pi * (r ** 2)

    return count_area


our_world = circle_area(3.14159, "OUR!")
print(f"our {our_world(1)}")
print(f"our {our_world(5)}")
print(f"our {our_world(5.85)}")

their_world = circle_area(4.14159, "THEIR")
print(f"their {their_world(1)}")
print(f"their {their_world(5)}")
print(f"their {their_world(5.85)}")
