my_dict = {
    "1": 1,
    "2": 0,
    "3": 3,
    "4": 0,
}

my_dict = {k: v for k, v in my_dict.items() if v != 0}

# for key, value in my_dict.items():
#     if value == 0:
#         del my_dict[key]
#         # my_dict.pop(key)


for key, value in dict(my_dict).items():
    if value == 0:
        del my_dict[key]


print(my_dict)
