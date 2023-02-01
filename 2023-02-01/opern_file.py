import os


FILE_PATH = "./test.txt"
base_name = os.path.basename(FILE_PATH)
dirname = os.path.dirname(__file__)
print(dirname)
print(base_name)
file_path = os.path.join(
    dirname, base_name
)
print(file_path)


# file = open(FILE_PATH, "w")
# try:
#     file.write("Hello World 1!\n")
#     1/0
# finally:
#     file.close()

name = "Joe"
# with open(FILE_PATH, "a") as file:
#     file.write(f"{name}\n")

with open(FILE_PATH, "a") as file:
    file.writelines([
        "abc\n",
        "123\n",
    ])

with open(FILE_PATH, "r") as file:
    # print(file.read())
    print(file.readlines())
