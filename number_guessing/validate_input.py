from utils import game_difficulties
from utils import get_range
from utils import try_conversion
from user_input import user_input


def validate(input_type, user_input):
    difficulties = game_difficulties()
    range_from_to = get_range()

    input_types = {
        'difficulty': user_input in list(difficulties.keys()),
        'guess': try_conversion(user_input) and int(user_input) in range(
            range_from_to['from'], range_from_to['to']
        )
    }

    return input_types.get(input_type)


def enforce_validation(input_type):

    if input_type == 'difficulty':
        selected_difficulty = user_input('difficulty')
        while not validate('difficulty', selected_difficulty):
            print('invalid input')
            selected_difficulty = user_input('difficulty')

        return selected_difficulty

    if input_type == 'guess':
        guess = user_input('guess')
        while not validate('guess', guess):
            print('out of range or not a number')
            guess = user_input('guess')

        return guess
