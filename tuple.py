t = ()
print(type(t))
one_element_tuple = (42, )
print(one_element_tuple)
three_element_tuple = (34, 45, 1)
print(three_element_tuple)
a, b, c = 1, 2, 3
print(a, b, c)
print(45 in three_element_tuple)

a1, b1 = 1, 2
c1 = a1
a1 = b1
b1 = c1
print(a1, b1)

a2, b2 = 0, 1
a2, b2 = b2, a2
print(a2, b2)