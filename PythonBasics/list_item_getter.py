from operator import itemgetter

a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
print(f'Sorting list to be sorted by numeric value: {a}')
print(f'Sorted list using sorted(): {sorted(a)}')
print(f'Sorted list using sorted(a, key=itemgetter(0): {sorted(a, key=itemgetter(0))}')    # which element of the tuple is sorted by
print(f'Sorted list using sorted(a, key=itemgetter(1)): {sorted(a, key=itemgetter(1))}')    # which element of the tuple is sorted by
print(f'Sorted list using sorted(a, key=itemgetter(1), reverse=True): {sorted(a, key=itemgetter(1), reverse=True)}')    # which element of the tuple is sorted by




