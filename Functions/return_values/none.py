# return none

def func():
    pass


func()      # this is not collected, aka lost
a = func()  # return is collected into a
print(a)
