test_var = "Test value"


def get_user_status(user="", auth=""):
    print(locals())
    requests.get("http://..", params={
        "Auth": auth,
    })


def my_func_2(*args, **kwargs):
    print(locals())
    print(args[0])


get_user_status(
    1, 15, 99, 2, 3, d=15, e=125, var="123", foo=125
)

# my_func_2(
#     1, 2, 3, var="123", foo=99
# )
