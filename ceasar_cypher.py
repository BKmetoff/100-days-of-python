import string


def letters():
    return list(string.ascii_lowercase)


def operations():
    return ["encrypt", "decrypt"]


def input_types():
    return ["word", "step", "operation"]


def user_input(input_type):
    input_options = input_types()

    prompt_types = {
        input_options[0]: "word to encrypt",
        input_options[1]: "encryption step",
        input_options[2]: f"to encrypt or decrypt"
    }

    return input(f'Choose {prompt_types[input_type]}:\n')


def encrypt_or_decrypt(word, step, operation):
    list_of_letters = letters()
    encryption_operations = operations()
    step = int(step)
    result = ''

    for letter in word:
        alphabet_index = list_of_letters.index(letter)

        if operation == encryption_operations[0]:
            result += list_of_letters[alphabet_index + step]
        else:
            result += list_of_letters[alphabet_index - step]

    return result


def exectute():
    encryption_operations = operations()
    input_options = input_types()

    word = user_input(input_options[0])

    step = user_input(input_options[1])
    while step not in string.digits:
        print("Only numbers allowed!")
        step = user_input(input_options[1])

    operation = user_input(input_options[2])
    while operation not in encryption_operations:
        print(
            f"Allowed inputs: {encryption_operations[0]}, {encryption_operations[1]}"
        )

        operation = user_input("operation")

    print(encrypt_or_decrypt(word, step, operation))


exectute()
