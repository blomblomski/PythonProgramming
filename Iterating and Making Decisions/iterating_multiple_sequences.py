people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
nationalities = ['Poland', 'India', 'South Africa', 'England']


for position in range(len(people)):     # Inefficient code / not Pythonic
    person = people[position]
    age = ages[position]
    print(position+1, person, age)

print('\n')

for position, person in enumerate(people):
    age = ages[position]
    print(position+1, person, age)

print('\n')

for person, age in zip(people, ages):
    print(person, age)

print('\n')

for person, age, nationality in zip(people, ages, nationalities):
    print(person, age, nationality)

print('\n')

for data in zip(people, ages, nationalities):
    person, age, nationality = data
    print(person, age, nationality)
