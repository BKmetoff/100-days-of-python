# make 'divisible' even more generic
# by passing multiple divisors as an array instead?
# loop through each divisor in the array
# and call a new function to do the modulo division?

def divisible(number, divisor1, divisor2=None):
    if divisor2 is None:
        return number % divisor1 == 0
    else:
        return number % divisor1 == 0 and number % divisor2 == 0


def loop(range):
    for num in range:
        if divisible(num, 3, 5):
            print("FizzBuzz")
        elif divisible(num, 3):
            print("Fizz")
        elif divisible(num, 5):
            print("Buzz")
        else:
            print(num)


print("======================")

loop(range(1, 101))
