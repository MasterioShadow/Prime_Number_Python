import math

# Function to check if a number is prime
def is_prime(num):
    # Handle boundary cases:
    if num <= 1:            # 1, 0 and -ve aren't primes
        return False
    elif num <= 3:          #anything in between 1 and 4 is prime for sure (2,3)
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    
    # Check odd divisors up to the square root of num (rounded up).
    for i in range(3, math.isqrt(num) + 1, 2):
        if num % i == 0:
            return False
    return True

# Input validation loop
while True:
    try:
        num = int(input('\n Please provide an integer to check for primality: '))
        break
    except ValueError:
        print("Invalid input data type! You must enter an integer.")

# Check if the provided number is prime
if is_prime(num):
    print("\n", num, 'is a prime number \n')
else:
    print("\n", num, 'is not a prime number \n')
