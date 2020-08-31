# filter regular
def is_multiple_of_five(n):
    return not n % 5


def get_multiple_of_five(n):
    return list(filter(is_multiple_of_five, range(n)))


print(is_multiple_of_five(13))
print(get_multiple_of_five(15))
