x = 3


def func(x):
    x = 7   # local x does not change global x


func(x)
print(x)
