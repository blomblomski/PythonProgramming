small_primes = set()
print(small_primes)

small_primes.add(2)
small_primes.add(3)
small_primes.add(5)
print(small_primes)
small_primes.add(1)
print(small_primes)
small_primes.remove(1)
print(small_primes)
print(3 in small_primes)
print(4 in small_primes)
small_primes.add(3)
print(small_primes)
bigger_prime = set([5, 7, 11, 13])
print(bigger_prime)
print(small_primes | bigger_prime)  # '|' union operator
print(small_primes & bigger_prime)
print(small_primes - bigger_prime)
