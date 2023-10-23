def prime_checker(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    max_divisor = int(num ** 0.5) + 1
    for i in range(3, max_divisor, 2):
        if num % i == 0:
            return False

    return True

# Input number to check for primality
number = int(input("Enter a number: "))

if prime_checker(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
