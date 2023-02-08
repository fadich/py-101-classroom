import random

from functools import partial


MIN_INT_VAL = -99
MAX_INT_VAL = 99
ARRAY_SIZE = 10

rand_int = partial(random.randint, a=MIN_INT_VAL, b=MAX_INT_VAL)
my_numbers = [rand_int() for _ in range(ARRAY_SIZE)]

print(my_numbers)

"""It's forbidden to use:
- sum
- count
- min / max
- sort / sorted
- list/set/dict/generator comprehensions
- generators
- modules (only functools is allowed)

"""

array_sum = ...
array_sub = ...
array_mul = ...

min_number = ...
max_number = ...

array_odds = ...
array_evens = ...

array_sqrs = ...

array_sqrs_avg = ...

print(
    f"array_sum = {array_sum}",
    f"array_sub = {array_sub}",
    f"array_mul = {array_mul}",
    f"min_number = {min_number}",
    f"max_number = {max_number}",
    f"array_odds = {array_odds}",
    f"array_evens = {array_evens}",
    f"array_sqrs = {array_sqrs}",
    f"array_sqrs_avg = {array_sqrs_avg}",
    sep="\n"
)

# Implementations

from functools import reduce


min_number = reduce(lambda x, y: x if x < y else y, my_numbers)
max_number = reduce(lambda x, y: x if x > y else y, my_numbers)

array_sum = reduce(lambda x, y: x + y, my_numbers)
array_sub = reduce(lambda x, y: x - y, my_numbers)
array_mul = reduce(lambda x, y: x * y, my_numbers, 1)

array_odds = list(filter(lambda x: x % 2, my_numbers))
array_evens = list(filter(lambda x: x % 2 == 0, my_numbers))

array_sqrs = list(map(lambda x: x ** 2, my_numbers))

array_sqrs_avg = reduce(lambda x, y: x + y, array_sqrs) / ARRAY_SIZE

print(
    f"array_sum = {array_sum}",
    f"array_sub = {array_sub}",
    f"array_mul = {array_mul}",
    f"min_number = {min_number}",
    f"max_number = {max_number}",
    f"array_odds = {array_odds}",
    f"array_evens = {array_evens}",
    f"array_sqrs = {array_sqrs}",
    f"array_sqrs_avg = {array_sqrs_avg}",
    sep="\n"
)
