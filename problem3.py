# Check if number is prime (1 is not prime)
def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

factors = []
target = int(input('What is the target number:\n'))
factor = 2

# Check every prime number if target number is divisible by it. If so, append to factors array, perform division, rince and repeat until target == 1.
# Be careful of rechecking every number if it's divisible again
while target != 1:
    if is_prime(factor) and target % factor == 0:
        factors.append(factor)
        target = target / factor
        continue
    factor += 1

print(factors)

