from utils import game_difficulties


def user_input(input_type):
    difficulties = "/".join(list(game_difficulties().keys()))

    if input_type == 'difficulty':
        return input(f"Select difficulty: {difficulties}\n")

    elif input_type == 'guess':
        return input("Make a guess:\n")
