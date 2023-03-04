
class Greeter:

    def __enter__(self):
        print("Hello")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Bye...")


greeting = Greeter()

with greeting:
    print("World")
    print("!!!")

print("After all")
