import json
import os.path


CONTACTS_FILEPATH = "./contacts.json"

contacts = {}
if os.path.exists(CONTACTS_FILEPATH):
    if not os.path.isfile(CONTACTS_FILEPATH):
        raise FileNotFoundError(f"{CONTACTS_FILEPATH} is not a file")

    with open(CONTACTS_FILEPATH, "r") as file:
        contacts = json.load(file)
        print()
        ...
        ...
    ...

record = {
    "name": "Tester",
    "phone": "+012345678901",
}

contacts[record["phone"]] = record

with open(CONTACTS_FILEPATH, "w") as file:
    json.dump(contacts, file)
