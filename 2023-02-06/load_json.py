import json


with open("user_list_sample.json", "r") as file:
    user_list_file = json.load(file)

print(user_list_file)

with open("user_list_sample.json", "r") as file:
    user_list_string = json.loads(file.read())


print(user_list_string)
