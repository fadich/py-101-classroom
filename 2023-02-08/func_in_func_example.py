
def circle_area(pi):
    def count_area(r):
        return pi * (r ** 2)

    return count_area


our_world = circle_area(3.14159)
print(f"our {our_world(1)}")
print(f"our {our_world(5)}")
print(f"our {our_world(5.85)}")

their_world = circle_area(4.14159)
print(f"their {their_world(1)}")
print(f"their {their_world(5)}")
print(f"their {their_world(5.85)}")
