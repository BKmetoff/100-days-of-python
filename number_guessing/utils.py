def game_difficulties():
    return {
        'normal': {'attempts': 10},
        'hard': {'attempts': 5}
    }


def get_range():
    return {'from': 0, 'to': 100}


def try_conversion(user_input):
    try:
        int(user_input)
    except:
        return False
    return True


def guess_is_correct(num_to_guess, guess):
    return int(guess) == int(num_to_guess)
