def counter(func):
    called_times = 0

    def wrap(*args, **kwargs):
        nonlocal called_times

        called_times += 1

        wrap.__called_times__ = called_times

        return func(*args, **kwargs)

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
    f"\nprint called: {...} time(s)",
    f"input called: {...} time(s)",
    sep="\n",
)



print(
    f"\nprint called: {print.__called_times__} time(s)",
    f"input called: {input.__called_times__} time(s)",
    sep="\n",
)
