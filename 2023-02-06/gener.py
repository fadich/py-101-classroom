print(__name__)

li = [i for i in [1, 2, 3, 4]]

print(li)
print(type(li))

gen = (i ** 2 for i in [1, 2, 3, 4])

print(gen)
print(type(gen))

for num in gen:
    print(num)

if __name__ == "__main__":
    print(123)
