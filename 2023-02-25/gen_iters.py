big_data = [1, 2, 3, 4]  # 1Tb

# b = (i for i in big_data)


def gen():
    yield 1
    yield 2
    yield 3
    yield 4


b = gen()
# print(b)
#
# print(next(b))
# print(next(b))


# b_iter = iter(b)
# while True:
#     try:
#         print(next(b_iter))
#     except StopIteration:
#         break


class Iterator:

    def __iter__(self):
        ...

    def __next__(self):
        ...


class Iter:

    def __init__(self, data, callback):
        # self._data = iter(data)
        self._index = 0
        self._max_value = 20
        self.callback = callback

    def __iter__(self):
        return self

    def __next__(self):
        # if self._index < len(self._data):
        #     val = self._data[self._index]
        #     self._index += 1
        #
        #     return val

        # return self.callback(next(self._data))

        if self._index < self._max_value:
            val = self._index
            self._index += 1
            return val

        raise StopIteration()

    def reset(self):
        self._index = 0


if __name__ == "__main__":
    iterator = Iter(big_data)

    for item in iterator:
        print(item)

    iterator.reset()
    for item in iterator:
        print(item)
