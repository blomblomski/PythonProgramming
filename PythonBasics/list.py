x = [1, 2, 3]
print('This is a list in python []:', x)
print('Python is magic: [i + 5for i in [2, 3, 4]]', [i + 5 for i in [2, 3, 4]])
print('Create a list from a tuple, list([1, 2, 3]):', list([1, 2, 3]))
print('Create a list from a sting, list("Hello"):', list("Hello"))

a = [1, 2, 3, 4]
print(f"Append new integer value to list a { a }:")     # we can append anything at the end
a.append(13)
print(a)
a.extend([5, 7])    # extend a list by adding two list together
print('This list has been extended', a)
print(f"Get index of list a[2]: {a[2]}")
a.insert(0, 17)
print(f"Insert value 17 at index zero, list: {a}")
print(f"Remove and return last element with pop, {a.pop()}")
print(f"Remove and return last element at index zero with pop, {a.pop(0)}")
a.remove(5)
print(f"Remove element from a list with remove(), {a} ")
a.reverse()
print(f"Reverse the order of the list with reverse(), {a}")
a.clear()
print(f"Clear the list with clear(), [] represents an empty list: {a}")

