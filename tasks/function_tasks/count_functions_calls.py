def counter(func):
    def wrap(*args, **kwargs):
        wrap.__counter__ += 1

        return func(*args, **kwargs)

    wrap.__counter__ = 0

    return wrap


input = counter(input)
print = counter(print)


first_name = input("First name: ")
last_name = input("Last name: ")

while True:
    age = input("Age: ")
    if age.isdigit():
        age = int(age)
        break

    print("Invalid age value")

print(
    f"\nFirst name: {first_name}",
    f"Last name: {last_name}",
    f"Age: {age}",
    sep="\n",
)

print(
    f"\nprint called: {print.__counter__} time(s)",
    f"input called: {input.__counter__} time(s)",
    sep="\n",
)
