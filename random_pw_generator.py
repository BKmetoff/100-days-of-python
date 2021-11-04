# Password Generator Project

# generate a string consisting of letters, numbers and symbols.
# the user chooses how many chars of each type should be included.
# all chars are ordered randomly.


import random
import string


def generate_char_types():
    return ["letters", "numbers", "symbols"]


def generate_chars():
    char_types = generate_char_types()

    return {
        char_types[0]: string.ascii_lowercase + string.ascii_uppercase,
        char_types[1]: list(string.digits),
        char_types[2]: list(string.punctuation),
    }


def char_type_prompt(char_type):
    return int(input(f"How many {char_type}:\n"))


def user_input():
    char_types = generate_char_types()

    letters = char_type_prompt(char_types[0])
    symbols = char_type_prompt(char_types[1])
    numbers = char_type_prompt(char_types[2])

    return {
        "total_length": letters + numbers + symbols,
        str(char_types[0]): letters,
        str(char_types[1]): symbols,
        str(char_types[2]): numbers
    }


def random_char(char_set):
    return char_set[random.randint(0, len(char_set) - 1)]


def generate_random_chars(char_set, num_of_needed_chars):

    # create string of random chars
    # of length specified by the user.

    chars = ""
    for ch in range(0, num_of_needed_chars):
        chars += random_char(char_set)

    return chars


def generate_password_template(length):

    # hepler function:
    # create array with length of len(user_input["total_length"]).
    # fill with unique numbers from 0 to (len(password) - 1).
    # these numbers will be used as indexes in randomize funcion
    # to point to chars in password variable.

    password_template = []
    while len(password_template) != length:
        num = random.randint(0, length - 1)
        if num in password_template:
            continue
        else:
            password_template.append(num)

    return password_template


def randomize(non_randomized_string, template):

    # use each member of 'template'
    # as an index of a char in non_randomized_password
    # to simulate randomization.

    randomized_password = ""
    for index in range(0, len(template)):
        char_index = int(template[index])
        randomized_password += non_randomized_string[char_index]

    return randomized_password


def generate_randomized_password(user_input):
    print(user_input)

    char_types = generate_char_types()
    chars = generate_chars()

    # append random chars in order.
    password = ""
    password += generate_random_chars(
        chars[char_types[0]],
        user_input[char_types[0]]
    )

    password += generate_random_chars(
        chars[char_types[1]],
        user_input[char_types[1]]
    )

    password += generate_random_chars(
        chars[char_types[2]],
        user_input[char_types[2]]
    )

    # randomise orderded string using 'password_template' helper.
    password_template = generate_password_template(user_input["total_length"])
    randomized_password = randomize(password, password_template)

    return randomized_password


def execute():
    print("Welcome to the PyPassword Generator!")
    print(f"Your password is: {generate_randomized_password(user_input())}")


print(execute())
