items = [0, None, 0.0, True, 0, 7]

found = False  # this is called 'flag'
for item in items:
    print('scanning item',  item)
    if item:
        found = True    # update the flag
        break

if found:
    print('At least one item evaluates to True')
else:
    print('All item evaluates to False')
