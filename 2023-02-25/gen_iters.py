big_data = [1, 2, 3, 4]  # 1Tb

# b = (i for i in big_data)


def gen():
    yield 1
    yield 2
    yield 3
    yield 4


b = gen()
print(b)

print(next(b))
print(next(b))


# while True:
#     try:
#         print(next(b))
#     except StopIteration:
#         break


