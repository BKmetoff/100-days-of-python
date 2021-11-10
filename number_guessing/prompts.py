from utils import get_range


def prompt(prompt_type, attempts=None):
    range_from_to = get_range()
    prompt_types = {
        'intro': f"This be da Numbah Guessing Game!\nGuess a number between {range_from_to['from']} and {range_from_to['to']}\n",
        'low': '\nToo low',
        'high': '\nToo high',
        'attempts': f'\n{attempts} attempts remaining\n',
        'win': 'Correct! You win!',
        'lose': 'No more attempts. You lose!',
    }

    print(prompt_types.get(prompt_type))
