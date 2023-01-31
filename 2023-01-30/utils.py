
class FloatCastingError(ValueError):
    pass


def to_float(string):
    try:
        return float(string)
    except ValueError:
        # return None
        raise FloatCastingError(f"Invalid value: {string}")


if __name__ == '__main__':
    value = to_float("1.0")
    print(value)
    print(type(value))

    assert to_float("1.0") == 1.0
    print(to_float("1.0") == 0.5)
    #    assert to_float("1.0") == 0.5
    assert True

    # result = to_float("1.0") == 1.0
    # if False:
    #     pass
    # else:
    #     raise AssertionError
