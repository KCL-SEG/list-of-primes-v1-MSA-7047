"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    num = 2
    while len(list) < number_of_primes:         # makes sure the list is equal to the given parameter 
        if is_prime(num):
            list.append(num)
        num += 1
    print(list)
    return list

def is_prime(n):            # checks if a number is prime, returns True if it is and False if not
    if n == 2 or n == 3:
        return True
    elif n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True