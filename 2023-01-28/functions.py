
def append_to_list(*args, c=None, line="line"):
    if c is None:
        c = []

    for arg in args:
        c.append(arg)

    return c
    # print(c)
    # print(line)


a = []

append_to_list(1, c=a)
append_to_list(2, c=a)
print(append_to_list(3, line="NEW", c=[1, 2, ]))
append_to_list(4)

print(a)
