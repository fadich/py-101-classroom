from typing import List


class Wall:
    pass


class Furniture:
    pass


class Room:

    def __init__(self, wall_amount: int):
        # Composition
        self._walls: List[Wall] = [Wall() for _ in range(wall_amount)]

        # Aggregation
        self._furniture: List[Furniture] = []

    @property
    def furniture(self):
        return self._furniture

    def __del__(self):
        for _ in range(len(self._walls)):
            self._walls.pop()


if __name__ == "__main__":
    table = Furniture()

    room = Room(4)
    sofa = Furniture()

    room.furniture.append(table)
    room.furniture.append(sofa)

    del room
