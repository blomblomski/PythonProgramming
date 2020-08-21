# integers are immutable
l_age = 42
print(id(l_age))

# this is a new integer object
l_age = 43
print(id(l_age))


class Person:
    def __init__(self, age):
        self.age = age

    def print_detail(self):
        print(id(self))
        print('age: '
              + str(person.age)
              + ' id: '
              + str(id(person.age)))


person = Person(42)
person.print_detail()

person.age = 120
person.print_detail()



