a = list('hello')
print(f'Made list from string hello, {a}')
a.append(100)
print(f'Can append integer (100) to list of strings, {a}')
a.extend((1, 2, 3))
print(f'Can be extended using tuples, {a}')
a.extend('...')
print(f'Extended by a string (...), {a}')