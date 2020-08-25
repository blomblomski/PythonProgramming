x = [1, 2, 3]


def func(x):
    x[1] = 42   # this affects the caller!
    x = 'this is something else'    # x points to a new object string


func(x)
print(x)