from utils import to_float, FloatCastingError


def read_float(prompt):
    while True:
        val = input(prompt)
        try:
            return to_float(val)
        except FloatCastingError as e:
            print(str(e))


def main():
    a = read_float("Insert A value: ")
    b = read_float(">>> ")

    try:
        print(f"{a} / {b} = {a / b}")
    # except ZeroDivisionError:
    #     print("Zero division error")
    except ArithmeticError as e:
        print(f"Error: {e}")
    finally:
        print("\nCalculation completed successfully")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n!!! Interrupted")
    finally:
        print("Goodbye!")
