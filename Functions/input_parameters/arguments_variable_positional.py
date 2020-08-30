def minimum(*n):
    # print(type(n)) n is type tuple
    if n:   # checks if n is empty
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)


minimum(1, 3, -7, 9)
minimum()

