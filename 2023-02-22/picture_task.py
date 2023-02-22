from typing import Tuple, List


class Pixel:
    COLOR_MIN = 0
    COLOR_MAX = 255

    OPACITY_MIN = 0.0
    OPACITY_MAX = 1.0

    def __init__(self, color: Tuple[int, int, int], opacity: float = 1.0):
        self.color = color
        self.opacity = opacity

    def __add__(self, other):
        if not isinstance(other, Pixel):
            raise TypeError()

        c = []
        for s, o in zip(self.color, other.color):
            c.append(s + o)

        op = self._check_opacity(self.opacity + other.opacity)
        new_c = tuple(map(self._check_color, c))

        return self.__class__(new_c, opacity=op)

    def __sub__(self, other):
        if not isinstance(other, Pixel):
            raise TypeError()

        c = []
        for s, o in zip(self.color, other.color):
            c.append(s - o)

        op = self._check_opacity(self.opacity - other.opacity)
        new_c = tuple(map(self._check_color, c))

        return self.__class__(new_c, opacity=op)

    def __eq__(self, other):
        if not isinstance(other, Pixel):
            return False

        return all(map(lambda c: c[0] == c[1], zip(self.color, other.color)))

    @classmethod
    def _check_color(cls, val: int):
        if val > cls.COLOR_MAX:
            return cls.COLOR_MAX

        if val < cls.COLOR_MIN:
            return cls.COLOR_MIN

        return val

    @classmethod
    def _check_opacity(cls, val: float):
        if val > cls.OPACITY_MAX:
            return cls.OPACITY_MAX

        if val < cls.OPACITY_MIN:
            return cls.OPACITY_MIN

        return val


class Picture:

    def __init__(self, pixels: List[List[Pixel]]):
        self.pixels = pixels

    def __add__(self, other: "Picture"):
        if not isinstance(other, Picture):
            raise TypeError()

        pixels = []
        for row_s, row_o in zip(self.pixels, other.pixels):
            rows = []
            for pix_s, pix_o in zip(row_s, row_o):
                rows.append(pix_s + pix_o)
            pixels.append(rows)

        return self.__class__(pixels)

    def __sub__(self, other):
        if not isinstance(other, Picture):
            raise TypeError()

        pixels = []
        for row_s, row_o in zip(self.pixels, other.pixels):
            rows = []
            for pix_s, pix_o in zip(row_s, row_o):
                rows.append(pix_s - pix_o)
            pixels.append(rows)

        return self.__class__(pixels)

    def __eq__(self, other):
        if not isinstance(other, Picture):
            return False

        for row_s, row_o in zip(self.pixels, other.pixels):
            for pix_s, pix_o in zip(row_s, row_o):
                if pix_s != pix_o:
                    return False

        return True


pxls_1 = [
    [Pixel((0, 25, 255)), Pixel((255, 25, 200)), Pixel((0, 25, 150))],
    [Pixel((0, 25, 255)), Pixel((255, 25, 200)), Pixel((0, 25, 150))],
    [Pixel((0, 25, 255)), Pixel((255, 25, 200)), Pixel((0, 25, 150))],
]

pxls_2 = [
    [Pixel((0, 255, 0)), Pixel((255, 25, 200)), Pixel((0, 25, 150))],
    [Pixel((0, 255, 0)), Pixel((255, 25, 200)), Pixel((0, 25, 150))],
    [Pixel((0, 255, 255)), Pixel((255, 25, 200)), Pixel((0, 25, 150))],
]

pxls_add = [
    [Pixel((0, 255, 255)), Pixel((255, 50, 255)), Pixel((0, 50, 255))],
    [Pixel((0, 255, 255)), Pixel((255, 50, 255)), Pixel((0, 50, 255))],
    [Pixel((0, 255, 255)), Pixel((255, 50, 255)), Pixel((0, 50, 255))],
]

pxls_sub = [
    [Pixel((0, 0, 255)), Pixel((0, 0, 0)), Pixel((0, 0, 0))],
    [Pixel((0, 0, 255)), Pixel((0, 0, 0)), Pixel((0, 0, 0))],
    [Pixel((0, 0, 0)), Pixel((0, 0, 0)), Pixel((0, 0, 0))],
]

assert Picture(pxls_1) + Picture(pxls_2) == Picture(pxls_add)
assert Picture(pxls_1) - Picture(pxls_2) == Picture(pxls_sub)
