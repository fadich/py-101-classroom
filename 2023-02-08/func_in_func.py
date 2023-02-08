
def func(fun, *args, **kwargs):
    return fun(*args, **kwargs)
    # return print(1, 2)


def outer(fun):
    print("OUTER CALLED")

    def inner(*args, **kwargs):
        print("INNER CALLED")

        return fun(*args, **kwargs)

    return inner


func_print = func(print, 1, 2)
print(func_print)

func_outer = outer(print)

print(func_outer)
print(type(func_outer))

func_outer("func_outer called")

outer(print)("outer called twice")
