people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]


for position in range(len(people)):     # Inefficient code / not Pythonic
    person = people[position]
    age = ages[position]
    print(position+1, person, age)

print('\n')

for position, person in enumerate(people):
    age = ages[position]
    print(position+1, person, age)
