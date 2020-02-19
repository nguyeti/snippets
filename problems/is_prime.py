# The following method checks if a number is prime by checking for divisibility on numbers less than it. It only
# needs to go up to the square root of n because if n is divisible by a number greater than its square root then
# it's divisible by something smaller than it.
# For example, while 33 is divisible by 11 (which is greater than the square root of 33), the "counterpart"to 11
# is 3 (3 * 11 = 33). 33 will have already been eliminated as a prime number by 3.
import math
def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(33))

# This runs in O( vn) time.