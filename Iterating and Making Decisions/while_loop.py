n = 39
remainders = []
while n > 0:
    remainder = n % 2
    remainders.insert(0, remainder)
    n //= 2  # divide by 2

print(remainders)