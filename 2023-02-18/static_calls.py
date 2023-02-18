
names = [
    "eduard",
    "fadi",
    "gendalf"
]

names_titled = (name.title() for name in names)
print(list(names_titled))

names_titled = map(lambda name: name.title(), names)
print(list(names_titled))

names_titled = map(str.title, names)
print(list(names_titled))

names_titled = (str.title(name) for name in names)
print(list(names_titled))


print(1 + 2)
print(int.__add__(1, 2))
print(int(1).__add__(2))
