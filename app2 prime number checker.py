import math

# Prompt the user to input the number they want to check for primality.
while True:
    try:
        num = int(input(
            'Please provide the number you\'d like to determine whether it\'s prime or not: '))
    except ValueError:
        print("\nInvalid input data type! You must enter an integer.\n")
    else:
        break
# Handle boundary cases:
# 1, 0 and -ve aren't primes, and 2 is prime, so check these conditions first.
if num <= 1:
    print("\n", num, 'is not a prime number \n')
elif num == 2:
    print("\n", num, 'is a prime number \n')
# If num is even, it's not prime (except for 2).
elif num % 2 == 0:
    print("\n", num, 'is not a prime number')
else:
    # Initialize a variable to track primality.
    is_prime = True
    # Check odd divisors up to the square root of num.
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            # If num is divisible by i, it's not prime.
            is_prime = False
            break

    # Determine and print the result.
    if is_prime:
        print("\n", num, 'is a prime number \n')
    else:
        print("\n", num, 'is not a prime number \n')
