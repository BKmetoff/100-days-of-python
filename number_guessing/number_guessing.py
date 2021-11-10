import random

from prompts import prompt
from validate_input import enforce_validation

from utils import game_difficulties
from utils import get_range
from utils import guess_is_correct


def execute():
    difficulties = game_difficulties()
    range_from_to = get_range()
    number_to_guess = random.randint(
        range_from_to['from'], range_from_to['to']
    )
    print(number_to_guess)

    prompt('intro')

    selected_difficulty = enforce_validation('difficulty')
    prompt('attempts', difficulties[selected_difficulty]['attempts'])

    guess = enforce_validation('guess')

    while not guess_is_correct(number_to_guess, guess):
        difficulties[selected_difficulty]['attempts'] -= 1

        if difficulties[selected_difficulty]['attempts'] == 0:
            prompt('lose')
            quit()

        prompt('low') if int(guess) < int(number_to_guess) else prompt('high')
        prompt('attempts', difficulties[selected_difficulty]['attempts'])

        guess = enforce_validation('guess')

    prompt('win')
    quit()


execute()
