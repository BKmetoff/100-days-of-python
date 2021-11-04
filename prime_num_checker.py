def remainder(number, divisor):
    return number % divisor == 0


def check(number):
    is_prime = True
    for n in range(2, number-1):
        if remainder(number, n):
            is_prime = False
            return is_prime

    return is_prime


def user_input():
    user_input = input("Choose number: ")

    try:
        int(user_input)
    except:
        print("not a number.")
        quit()

    return int(user_input)


def execute():
    is_prime = (check(user_input()))
    print(f"Number is{' ' if is_prime else ' not '}prime.")


execute()
