print("Lambda")


numbers = [str(i) for i in range(10)]

# b = [i ** 2 for i in numbers]
# c = (i ** 2 for i in numbers)
#
#
# def sqr(x):
#     return x ** 2
#
#
# g = (sqr(i) for i in numbers)
# m = map(sqr, numbers)
#
#
# def _(x):
#     return x ** 2


# lm = lambda x: x ** 2
# print(lm(10))

ml = map(lambda x: x ** 2, numbers)


# print(*numbers)
# print(numbers[0], numbers[1], ...)

# map_obj = map(lambda x: x if x > 0 else x ** 2, numbers)
map_obj = map(str.isdigit, numbers)
print(
    tuple(map_obj)
)


# import os
# os.listdir("")
