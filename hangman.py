import random
import string


def word_pool(): return ["ring", "banana", "phone"]


def letter_blanks(word): return "".join(["_" for letter in word])


def player_guess():
    guess = input("Your guess:\n")

    while guess not in string.ascii_letters or len(guess) != 1:
        print("Invalid input! One letter at a time only!")
        guess = input("Your guess:\n")

    return guess.lower()


def check_guess(word, guessed_letter, word_signature):
    updated_word_signature = list(word_signature)

    for index, letter_in_word in enumerate(word):
        if letter_in_word == guessed_letter:
            updated_word_signature[index] = guessed_letter

    return "".join(updated_word_signature)


def game_over(game_won):
    print(f"Game over, you {'won' if game_won else 'lose'}!")


def display_current_score(word_signature, remaining_lives):
    print(f"Word: {word_signature}\nRemaining lives: {remaining_lives}\n")


def execute():
    word_to_guess = random.choice(word_pool())
    word_signature = letter_blanks(word_to_guess)
    lives = len(word_to_guess)

    display_current_score(word_signature, lives)
    # print(word_to_guess, word_signature)

    while lives != 0:
        player_choice = player_guess()

        updated_signature = check_guess(
            word_to_guess, player_choice, word_signature
        )

        if updated_signature == word_signature:
            lives -= 1

        if updated_signature.count("_") == 0:
            return game_over(True)

        word_signature = updated_signature

        display_current_score(updated_signature, lives)

    game_over(False)


execute()
