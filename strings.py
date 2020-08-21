from math import pi

str1 = 'This is a single quote string'
str2 = "This is a double quote string"
str3 = ''' This is a triple quote string. 

    It can span a cross multiple lines.     
'''
str4 = 'A little bit of string\n\t\t\tformatting'

print(str1)
print(str2)
print(str3)
print(str4)

print(len(str3))

s = "This is a üŋíc0de"
print(type(s))
encoded_s = s.encode('utf-8')
print(encoded_s)
print(type(encoded_s))
print(encoded_s.decode('utf-8'))
bytes_obj = b"A bytes object"
print(type(bytes_obj))

str5 = "The trouble is you think you have time."
print(str5[0])
print(str5[5])
print(str5[:4])     # stop slicing at
print(str5[4:])     # start slicing at
print(str5[2:14])     # both start and stop positions
print(str5[2:14:3])     # start, stop and step
str6 = str5[:]  # make a copy of the string
print(str6)

greet_old = 'Hello %s!'     # deprecated use string format
print(greet_old % 'Kevin')

greet_positional = 'Hello {} {}!'
print(greet_positional.format('Kevin', 'Plover'))

greet_positional_idx = 'This is {0}! {1} loves {0}!'
print(greet_positional_idx.format('Python', 'Kevin'))
print(greet_positional_idx.format('Coffee', 'Kevin'))

keyword = 'Hello, my name is {name} {last_name}'
print(keyword.format(name='Kevin', last_name='Plover'))

name = 'Kevin'
age = 33
print(f"Hello! may name is {name} and I'm {age}")

print(f"No arguing with {pi}, it's irrational...")


