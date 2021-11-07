import string
import random


def game_difficulties():
    return {
        'normal': {'attempts': 10},
        'hard': {'attempts': 5}
    }


def validate(user_input):
    difficulties = game_difficulties()
    input_types = {
        # 'difficulty': str(user_input) in list(difficulties.keys()),
        'difficulty': str(user_input) in ['normal', 'hard'],
        'guess': user_input in string.digits and int(user_input) in range(0, 100)
    }

    return input_types.get(user_input)


def user_input(input_type):
    difficulties = list(game_difficulties().keys())

    if input_type == 'difficulty':
        return input(f"Select difficulty: {difficulties[0]}/{difficulties[1]}\n")

    elif input_type == 'guess':
        return input("Make a guess:\n")


def prompt(prompt_type, attempts=None):
    prompt_types = {
        'intro': 'This be da Numbah Guessing Game!\nGuess a number between 0 and 100\n',
        'low': '\nToo low',
        'high': '\nToo high',
        'attempts': f'\n{attempts} attempts remaining\n',
        'win': 'Correct! You win!',
        'lose': 'No more attempts. You lose!',
    }

    print(prompt_types.get(prompt_type))


def guess_is_correct(num_to_guess, guess):
    return int(guess) == int(num_to_guess)


def execute():
    difficulties = game_difficulties()
    number_to_guess = random.randint(0, 100)
    print(number_to_guess)

    prompt('intro')

    difficulty = user_input('difficulty')
    while not validate(difficulty):
        print('invalid input')
        guess = user_input('difficulty')

    prompt('attempts', difficulties[difficulty]['attempts'])

    guess = user_input('guess')
    while not validate(guess):
        print('out of range or not a number')
        guess = user_input('guess')

    while not guess_is_correct(number_to_guess, guess):
        difficulties[difficulty]['attempts'] -= 1

        if difficulties[difficulty]['attempts'] == 0:
            prompt('lose')
            quit()

        prompt('low') if int(guess) < int(number_to_guess) else prompt('high')
        prompt('attempts', difficulties[difficulty]['attempts'])
        guess = user_input('guess')

    prompt('win')
    quit()


execute()
