"""
JSON supports mainly 6 data types:
- string.
- number.
- boolean.
- null.
- object.
- array.
"""

import json

from pprint import pprint


# d = "{\"abc\": 1, }"  # INVALID (coma)
# d = "{'abc': 1}"  # INVALID (single quotes)
d = "{\"abc\": 1}"
n = "1"
f = "1.5"
null = "null"
array = "[1, 2, 3]"
boolean = "false"
string = "\"abc\""


# for i in (d, n, f, null, array, boolean, string):
#     print(json.loads(i))
#     print(type(json.loads(i)))


d = {
    "abc": 1,
    "something": [1, 2, 3, ],
}
n = 1
f = 1.75
null = None
array = [1, 2, 3]
boolean = True
string = "Hello world!"

# for i in (d, n, f, null, array, boolean, string):
#     print(repr(json.dumps(i)))
#     print(type(json.dumps(i)))


filepath = "./user_list_sample.json"

with open(filepath) as file:
    users_raw = file.read()


user_list: list = json.loads(users_raw)
pprint(user_list)

print()
user_hobbies = []
for user in user_list:  # type: dict
    hobbies = user.get("hobbies", [])
    user_hobbies.extend(hobbies)
    print(f"{user.get('name')}: {hobbies}")

print(user_hobbies)


print(json.dumps(user_list))
