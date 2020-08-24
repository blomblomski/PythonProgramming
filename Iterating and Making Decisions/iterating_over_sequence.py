surnames = ['Revist', 'Shamir', 'Adleman']
for position in range(len(surnames)):
    print(position + 1, surnames[position])

print('\n')

for surname in surnames:
    print(surname)

print('\n')

for position, surname in enumerate(surnames):
    print(position, surname)
