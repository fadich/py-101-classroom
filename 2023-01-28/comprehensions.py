users = database.User.get_users()

for user in users:
    ...

a = [
    f"{u.first_name or ''} {u.last_name or ''}"
    for u in database.User.get_users()
    if u.is_admin or ...
]

print(a)


import time

current_time = time.time()

a = []
for i in range(20_000_000):
    a.append(i)

print(f"t = {time.time() - current_time:.6f}")


current_time = time.time()

a = [i for i in range(20_000_000)]

print(f"t = {time.time() - current_time:.6f}")



