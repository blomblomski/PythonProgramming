# Local versus Global

def local():
    print(m, 'printing from the global scope')


m = 5
print(m, 'printing from the global scope')

local()
